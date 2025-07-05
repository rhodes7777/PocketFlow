import yaml
from pocketflow import Node
from utils.call_llm import call_llm
from utils.search_web import search_web

class DecideNode(Node):
    """
    Decides whether to search for more information or answer the question directly.
    """
    
    def prep(self, shared):
        user_prompt = shared["user_prompt"]
        previous_searches = shared.get("search_history", [])
        return user_prompt, previous_searches
        
    def exec(self, inputs):
        user_prompt, previous_searches = inputs
        
        # Format previous search context
        search_context = ""
        if previous_searches:
            search_context = "\n\nPrevious search results:\n"
            for i, search in enumerate(previous_searches, 1):
                search_context += f"Search {i}: {search['query']}\n"
                search_context += f"Results: {search['results'][:200]}...\n\n"
        
        prompt = f"""
You are an AI assistant that needs to decide whether to search for more information or answer a question directly.

User Question: {user_prompt}
{search_context}

Based on the question and any previous search results, decide whether you need to search for more current information or if you can answer directly with existing knowledge.

Consider searching if:
- The question asks for recent/current information
- The question is about specific facts, statistics, or events
- Previous searches didn't provide enough information
- The question is about breaking news or recent developments

Consider answering directly if:
- You have sufficient information from previous searches
- The question is about general knowledge that doesn't change frequently
- The question is conceptual or theoretical

Output your decision in YAML format:
```yaml
action: search/answer
reasoning: Brief explanation of your decision
search_query: What to search for (only if action is search)
```"""
        
        response = call_llm(prompt)
        
        # Parse YAML response
        try:
            yaml_content = response.split("```yaml")[1].split("```")[0].strip()
            result = yaml.safe_load(yaml_content)
            
            # Validate response
            assert isinstance(result, dict), "Response must be a dictionary"
            assert "action" in result, "Response must contain 'action' field"
            assert "reasoning" in result, "Response must contain 'reasoning' field"
            assert result["action"] in ["search", "answer"], "Action must be 'search' or 'answer'"
            
            if result["action"] == "search":
                assert "search_query" in result, "Search query required when action is 'search'"
            
            return result
            
        except Exception as e:
            # Fallback: if parsing fails, default to search
            return {
                "action": "search",
                "reasoning": f"Failed to parse decision: {str(e)}",
                "search_query": user_prompt
            }

    def post(self, shared, prep_res, exec_res):
        shared["last_decision"] = exec_res
        
        if exec_res["action"] == "search":
            shared["search_query"] = exec_res["search_query"]
            return "search"
        else:
            return "answer"

class SearchNode(Node):
    """
    Performs web search using DuckDuckGo and stores results.
    """
    
    def prep(self, shared):
        return shared["search_query"]
        
    def exec(self, search_query):
        results = search_web(search_query, max_results=5)
        return results
    
    def post(self, shared, prep_res, exec_res):
        # Store search results in history
        if "search_history" not in shared:
            shared["search_history"] = []
        
        shared["search_history"].append({
            "query": prep_res,
            "results": exec_res
        })
        
        # Go back to decide node to check if we have enough information
        return "decide"

class AnswerNode(Node):
    """
    Provides final answer based on user prompt and search context.
    """
    
    def prep(self, shared):
        user_prompt = shared["user_prompt"]
        search_history = shared.get("search_history", [])
        return user_prompt, search_history
        
    def exec(self, inputs):
        user_prompt, search_history = inputs
        
        # Format search context
        search_context = ""
        if search_history:
            search_context = "\n\nSearch Results:\n"
            for i, search in enumerate(search_history, 1):
                search_context += f"Search {i} - Query: {search['query']}\n"
                search_context += f"Results:\n{search['results']}\n\n"
        
        prompt = f"""
You are a helpful AI assistant. Answer the user's question based on the provided context and your knowledge.

User Question: {user_prompt}
{search_context}

Please provide a comprehensive and helpful answer to the user's question. If you used search results, cite them appropriately. Be clear, concise, and accurate.

Answer:"""
        
        response = call_llm(prompt)
        return response

    def post(self, shared, prep_res, exec_res):
        shared["final_answer"] = exec_res
        print(f"\nFinal Answer: {exec_res}")
        return "complete"
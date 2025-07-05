from pocketflow import Node
import yaml

from utils import call_llm, search_duckduckgo

class DecideNode(Node):
    """Decide whether to search the web or answer directly."""
    def prep(self, shared):
        question = shared["question"]
        context = shared.get("context", "No previous search")
        prompt = f"""
### CONTEXT
Question: {question}
Previous Research: {context}

### ACTION SPACE
- search: Look up more information on the web
- answer: Provide a final answer with current context

Return your response in this YAML format:
```yaml
action: search | answer
reason: <why>
search_query: <query if searching>
answer: <answer if answering>
```
"""
        return prompt

    def exec(self, prompt):
        response = call_llm(prompt)
        try:
            yaml_str = response.split("```yaml")[1].split("```", 1)[0]
            decision = yaml.safe_load(yaml_str)
        except Exception:
            decision = {"action": "answer", "answer": response}
        return decision

    def post(self, shared, prep_res, decision):
        if decision.get("action") == "search":
            shared["search_query"] = decision.get("search_query", shared["question"])
            return "search"
        shared["answer"] = decision.get("answer", "")
        return "answer"

class SearchWebNode(Node):
    """Search the web using DuckDuckGo."""
    def prep(self, shared):
        return shared.get("search_query", shared["question"])

    def exec(self, query):
        return search_duckduckgo(query)

    def post(self, shared, prep_res, results):
        shared["context"] = results
        return "decide"

class AnswerNode(Node):
    """Use the context to craft a final answer via OpenAI."""
    def prep(self, shared):
        question = shared["question"]
        context = shared.get("context", "")
        prompt = f"""
### CONTEXT
Question: {question}
Research: {context}

Provide a comprehensive answer."""
        return prompt

    def exec(self, prompt):
        return call_llm(prompt)

    def post(self, shared, prep_res, answer):
        shared["answer"] = answer
        return "done"

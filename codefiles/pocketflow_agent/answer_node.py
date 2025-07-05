"""
Answer Node for PocketFlow Agent
"""

from pocketflow import Node
from .utils import call_openai


class AnswerNode(Node):
    """
    Node that generates an answer using OpenAI based on the query and any search results.
    """
    
    def prep(self, shared):
        """
        Prepare the context for generating an answer
        
        Args:
            shared (dict): Shared store containing query and optional search results
            
        Returns:
            tuple: (query, search_results)
        """
        query = shared.get("original_query", shared.get("query", ""))
        search_results = shared.get("search_result", "")
        
        return query, search_results
    
    def exec(self, prep_res):
        """
        Generate an answer using OpenAI
        
        Args:
            prep_res (tuple): (query, search_results)
            
        Returns:
            str: Generated answer
        """
        query, search_results = prep_res
        
        # Construct the prompt based on available information
        if search_results:
            prompt = f"""
Based on the following search results, please answer the question:

Question: {query}

Search Results: {search_results}

Please provide a comprehensive answer based on the search results.
"""
        else:
            prompt = f"""
Please answer the following question:

Question: {query}

Please provide a helpful answer based on your knowledge.
"""
        
        answer = call_openai(prompt)
        return answer
    
    def post(self, shared, prep_res, exec_res):
        """
        Store the final answer
        
        Args:
            shared (dict): Shared store
            prep_res (tuple): (query, search_results)
            exec_res (str): Generated answer
            
        Returns:
            str: Default action (flow will end here)
        """
        shared["answer"] = exec_res
        return "default"
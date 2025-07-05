"""
Search Node for PocketFlow Agent
"""

from pocketflow import Node
from .utils import search_duckduckgo


class SearchNode(Node):
    """
    Node that performs a search using DuckDuckGo and saves the result.
    Routes back to DecisionNode to allow for additional decisions.
    """
    
    def prep(self, shared):
        """
        Extract the query from shared store
        
        Args:
            shared (dict): Shared store containing query
            
        Returns:
            str: The query to search for
        """
        query = shared.get("query", "")
        return query
    
    def exec(self, prep_res):
        """
        Perform the search using DuckDuckGo
        
        Args:
            prep_res (str): The query to search for
            
        Returns:
            str: Search results
        """
        query = prep_res
        search_results = search_duckduckgo(query)
        return search_results
    
    def post(self, shared, prep_res, exec_res):
        """
        Save search results and route back to DecisionNode or answer if max searches reached
        
        Args:
            shared (dict): Shared store
            prep_res (str): The query string
            exec_res (str): The search results
            
        Returns:
            str: Action to route back to DecisionNode or to answer
        """
        # Store the search results
        shared["search_result"] = exec_res
        
        # Increment search count
        search_count = shared.get("search_count", 0) + 1
        shared["search_count"] = search_count
        max_searches = shared.get("max_searches", 2)
        
        # Update the query to include search context for next decision
        original_query = shared.get("original_query", shared.get("query", ""))
        shared["original_query"] = original_query  # Keep the original
        
        # If we've reached max searches, force answer
        if search_count >= max_searches:
            shared["query"] = f"{original_query} (with search results available - max searches reached)"
            return "answer"
        else:
            # Modify query to include search results for next decision
            shared["query"] = f"{original_query} (with search results available)"
            return "decide"
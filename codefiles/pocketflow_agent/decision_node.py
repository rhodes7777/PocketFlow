"""
Decision Node for PocketFlow Agent
"""

from pocketflow import Node


class DecisionNode(Node):
    """
    Node that decides whether to search or answer based on the input query.
    Returns "search" if "search" is in the input, otherwise "answer".
    """
    
    def prep(self, shared):
        """
        Extract the query from shared store
        
        Args:
            shared (dict): Shared store containing query
            
        Returns:
            str: The query string
        """
        query = shared.get("query", "")
        return query
    
    def exec(self, prep_res):
        """
        Decide action based on whether "search" is in the query
        
        Args:
            prep_res (str): The query string
            
        Returns:
            str: "search" or "answer"
        """
        query = prep_res.lower()
        
        # If "search" is in the query, return "search", otherwise "answer"
        if "search" in query:
            return "search"
        else:
            return "answer"
    
    def post(self, shared, prep_res, exec_res):
        """
        Store the decision and return the action
        
        Args:
            shared (dict): Shared store
            prep_res (str): The query string
            exec_res (str): The decision ("search" or "answer")
            
        Returns:
            str: The action to take
        """
        shared["decision"] = exec_res
        return exec_res
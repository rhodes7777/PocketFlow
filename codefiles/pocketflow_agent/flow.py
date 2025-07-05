"""
Flow definition for PocketFlow Agent
"""

from pocketflow import Flow
from .decision_node import DecisionNode
from .search_node import SearchNode
from .answer_node import AnswerNode


def create_agent_flow():
    """
    Create and return a configured agent flow.
    
    The flow works as follows:
    1. Start with DecisionNode which decides whether to search or answer
    2. If "search" action: go to SearchNode
    3. If "answer" action: go to AnswerNode
    4. SearchNode routes back to DecisionNode with "decide" action
    5. AnswerNode ends the flow
    
    Returns:
        Flow: Configured PocketFlow agent
    """
    
    # Create node instances
    decision_node = DecisionNode()
    search_node = SearchNode()
    answer_node = AnswerNode()
    
    # Define the flow connections
    # DecisionNode routes to SearchNode or AnswerNode based on decision
    decision_node - "search" >> search_node
    decision_node - "answer" >> answer_node
    
    # SearchNode routes back to DecisionNode for another decision
    search_node - "decide" >> decision_node
    
    # SearchNode can also route directly to AnswerNode if max searches reached
    search_node - "answer" >> answer_node
    
    # AnswerNode ends the flow (no successor defined)
    
    # Create the flow starting with DecisionNode
    flow = Flow(start=decision_node)
    
    return flow


def run_agent(query):
    """
    Convenience function to run the agent with a query
    
    Args:
        query (str): The query to process
        
    Returns:
        dict: The shared store containing the results
    """
    # Create shared store
    shared = {
        "query": query,
        "original_query": query,
        "decision": None,
        "search_result": None,
        "answer": None,
        "search_count": 0,  # Track number of searches to prevent infinite loops
        "max_searches": 2   # Maximum number of searches allowed
    }
    
    # Create and run the flow
    flow = create_agent_flow()
    flow.run(shared)
    
    return shared


if __name__ == "__main__":
    # Test the flow with different queries
    print("Testing with search query:")
    result1 = run_agent("search for information about Python programming")
    print(f"Decision: {result1['decision']}")
    print(f"Search Result: {result1['search_result']}")
    print(f"Answer: {result1['answer']}")
    
    print("\n" + "="*50 + "\n")
    
    print("Testing with direct question:")
    result2 = run_agent("What is machine learning?")
    print(f"Decision: {result2['decision']}")
    print(f"Search Result: {result2['search_result']}")
    print(f"Answer: {result2['answer']}")
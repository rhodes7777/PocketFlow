from pocketflow import Flow
from nodes import DecideNode, SearchNode, AnswerNode

def create_search_answer_flow():
    """
    Create and return a search-answer flow.
    
    Flow:
    1. Start with DecideNode - decides whether to search or answer
    2. If search needed, go to SearchNode
    3. SearchNode goes back to DecideNode to check if enough info
    4. If enough info, DecideNode goes to AnswerNode
    5. AnswerNode provides final answer
    """
    # Create nodes
    decide_node = DecideNode(max_retries=3, wait=1)
    search_node = SearchNode(max_retries=3, wait=1)
    answer_node = AnswerNode(max_retries=3, wait=1)
    
    # Connect nodes with actions
    decide_node - "search" >> search_node  # If decide to search, go to search
    decide_node - "answer" >> answer_node  # If decide to answer, go to answer
    search_node - "decide" >> decide_node  # After search, go back to decide
    
    # Create flow starting with decide node
    return Flow(start=decide_node)

def create_simple_flow():
    """
    Create a simpler version for testing individual components.
    """
    decide_node = DecideNode()
    search_node = SearchNode()
    answer_node = AnswerNode()
    
    # Simple linear flow for testing
    decide_node >> search_node >> answer_node
    
    return Flow(start=decide_node)
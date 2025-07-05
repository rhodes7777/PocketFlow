from pocketflow import Flow
from nodes import DecideNode, SearchWebNode, AnswerNode


def create_flow() -> Flow:
    """Assemble the three-node flow."""
    decide = DecideNode()
    search = SearchWebNode()
    answer = AnswerNode()

    decide - "search" >> search
    decide - "answer" >> answer
    search - "decide" >> decide

    return Flow(start=decide)

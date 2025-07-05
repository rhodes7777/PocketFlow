#!/usr/bin/env python3
"""
Simple test script for PocketFlow Agent
"""

import sys
sys.path.append('/workspace')

from pocketflow import Flow
from .utils import search_duckduckgo, call_openai
from .decision_node import DecisionNode
from .search_node import SearchNode
from .answer_node import AnswerNode


def test_utility_functions():
    """Test the utility functions"""
    print("=== Testing Utility Functions ===")
    
    # Test search function
    search_result = search_duckduckgo("Python programming")
    print(f"Search result: {search_result}")
    
    # Test OpenAI function
    ai_response = call_openai("What is machine learning?")
    print(f"AI response: {ai_response}")
    

def test_decision_node():
    """Test the decision node"""
    print("\n=== Testing Decision Node ===")
    
    node = DecisionNode()
    
    # Test with search query
    shared1 = {"query": "search for Python tutorials"}
    result1 = node.run(shared1)
    print(f"Query: '{shared1['query']}' -> Decision: {result1}")
    
    # Test with direct question
    shared2 = {"query": "What is machine learning?"}
    result2 = node.run(shared2)
    print(f"Query: '{shared2['query']}' -> Decision: {result2}")


def test_search_node():
    """Test the search node"""
    print("\n=== Testing Search Node ===")
    
    node = SearchNode()
    shared = {"query": "Python programming"}
    result = node.run(shared)
    print(f"Query: '{shared['query']}' -> Action: {result}")
    print(f"Search result stored: {shared.get('search_result', 'None')}")


def test_answer_node():
    """Test the answer node"""
    print("\n=== Testing Answer Node ===")
    
    node = AnswerNode()
    shared = {"query": "What is Python?", "search_result": ""}
    result = node.run(shared)
    print(f"Query: '{shared['query']}' -> Action: {result}")
    print(f"Answer: {shared.get('answer', 'None')}")


def test_simple_flow():
    """Test a simple flow without loops"""
    print("\n=== Testing Simple Flow (No Loops) ===")
    
    # Create nodes
    decision_node = DecisionNode()
    answer_node = AnswerNode()
    
    # Simple flow: decision -> answer (no search to avoid loops)
    decision_node - "answer" >> answer_node
    
    # Create flow
    flow = Flow(start=decision_node)
    
    # Test with a non-search query
    shared = {"query": "What is machine learning?"}
    flow.run(shared)
    
    print(f"Query: {shared['query']}")
    print(f"Decision: {shared.get('decision', 'None')}")
    print(f"Answer: {shared.get('answer', 'None')}")


if __name__ == "__main__":
    test_utility_functions()
    test_decision_node()
    test_search_node()
    test_answer_node()
    test_simple_flow()
    print("\n=== All tests completed ===")
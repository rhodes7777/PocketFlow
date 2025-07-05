#!/usr/bin/env python3
"""
Comprehensive test for PocketFlow Agent with full flow
"""

import sys
sys.path.append('/workspace')

from .flow import run_agent


def test_search_query():
    """Test with a query that triggers search"""
    print("=== Testing Search Query ===")
    
    query = "search for information about Python programming"
    result = run_agent(query)
    
    print(f"Original Query: {result['original_query']}")
    print(f"Final Query: {result['query']}")
    print(f"Decision: {result['decision']}")
    print(f"Search Count: {result['search_count']}")
    print(f"Search Result: {result['search_result'][:100]}..." if result['search_result'] else "None")
    print(f"Answer: {result['answer'][:100]}..." if result['answer'] else "None")
    print()


def test_direct_question():
    """Test with a direct question that doesn't trigger search"""
    print("=== Testing Direct Question ===")
    
    query = "What is machine learning?"
    result = run_agent(query)
    
    print(f"Original Query: {result['original_query']}")
    print(f"Final Query: {result['query']}")
    print(f"Decision: {result['decision']}")
    print(f"Search Count: {result['search_count']}")
    print(f"Search Result: {result['search_result']}")
    print(f"Answer: {result['answer'][:100]}..." if result['answer'] else "None")
    print()


def test_loop_prevention():
    """Test that the loop prevention mechanism works"""
    print("=== Testing Loop Prevention ===")
    
    # This query will trigger search, but the loop should be prevented
    query = "search search search for Python"  # Multiple "search" words
    result = run_agent(query)
    
    print(f"Original Query: {result['original_query']}")
    print(f"Final Query: {result['query']}")
    print(f"Decision: {result['decision']}")
    print(f"Search Count: {result['search_count']}")
    print(f"Max Searches: {result['max_searches']}")
    print(f"Search Result: {result['search_result'][:100]}..." if result['search_result'] else "None")
    print(f"Answer: {result['answer'][:100]}..." if result['answer'] else "None")
    print()


if __name__ == "__main__":
    test_search_query()
    test_direct_question() 
    test_loop_prevention()
    print("=== All comprehensive tests completed ===")
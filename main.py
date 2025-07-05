#!/usr/bin/env python3

import os
import sys
from flow import create_search_answer_flow

def main():
    """
    Main function to run the search-answer system.
    """
    # Check for required environment variables
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is required")
        print("Please set it with: export OPENAI_API_KEY='your-api-key'")
        return 1
    
    # Get user input
    if len(sys.argv) > 1:
        # Use command line argument
        user_prompt = " ".join(sys.argv[1:])
    else:
        # Interactive mode
        user_prompt = input("Enter your question: ")
    
    if not user_prompt.strip():
        print("Error: Please provide a question")
        return 1
    
    # Initialize shared data
    shared = {
        "user_prompt": user_prompt,
        "search_history": [],
        "final_answer": None
    }
    
    # Create and run the flow
    try:
        print(f"Processing question: {user_prompt}")
        print("-" * 50)
        
        flow = create_search_answer_flow()
        flow.run(shared)
        
        print("\n" + "=" * 50)
        print("RESULTS:")
        print("=" * 50)
        
        # Show search history if any
        if shared.get("search_history"):
            print(f"\nSearches performed: {len(shared['search_history'])}")
            for i, search in enumerate(shared['search_history'], 1):
                print(f"  {i}. {search['query']}")
        
        # Show final answer
        if shared.get("final_answer"):
            print(f"\nFinal Answer:\n{shared['final_answer']}")
        else:
            print("\nNo final answer was generated")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 1
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
import os
from openai import OpenAI

def call_llm(prompt):
    """
    Call OpenAI's GPT model with the given prompt.
    
    Args:
        prompt (str): The prompt to send to the LLM
        
    Returns:
        str: The response from the LLM
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Test the function
    test_prompt = "What is the capital of France?"
    print(f"Prompt: {test_prompt}")
    print(f"Response: {call_llm(test_prompt)}")
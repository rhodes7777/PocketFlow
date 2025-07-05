from duckduckgo_search import DDGS

def search_web(query, max_results=3):
    """
    Search the web using DuckDuckGo.
    
    Args:
        query (str): The search query
        max_results (int): Maximum number of results to return
        
    Returns:
        str: Formatted search results
    """
    try:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=max_results)
        
        if not results:
            return "No search results found."
        
        formatted_results = []
        for i, result in enumerate(results, 1):
            title = result.get('title', 'No title')
            body = result.get('body', 'No description')
            href = result.get('href', 'No URL')
            
            formatted_results.append(f"{i}. {title}\n{body}\nURL: {href}\n")
        
        return "\n".join(formatted_results)
    
    except Exception as e:
        return f"Error during search: {str(e)}"

if __name__ == "__main__":
    # Test the function
    test_query = "Python programming"
    print(f"Search Query: {test_query}")
    print(f"Results:\n{search_web(test_query)}")
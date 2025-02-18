#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers of a given subreddit.

This module uses the Reddit API to retrieve information about a subreddit, specifically
the number of subscribers. If the subreddit is valid, the subscriber count is returned.
If the subreddit does not exist or is invalid, the function returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers of a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    # Define the Reddit API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set the custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/yourusername)'}
    
    try:
        # Send a GET request to the Reddit API with custom headers and avoid following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the subreddit is invalid (404 status code), return 0
        if response.status_code == 404:
            return 0
        
        # Parse the JSON response
        data = response.json()
        
        # Return the number of subscribers from the 'data' field
        return data['data']['subscribers']
    
    except Exception:
        # Handle any exceptions (network issues, etc.) and return 0
        return 0



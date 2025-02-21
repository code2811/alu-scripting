#!/usr/bin/python3
"""
Module to query Reddit API and get top 10 hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
    
    Returns:
        None: Prints post titles or None if subreddit is invalid.
    """
    # Reddit API URL for hot posts in the specified subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Custom User-Agent to avoid too many requests error
    headers = {
        'User-Agent': 'linux:alu_api_script:v1.0 (by /u/alu_student)'
    }
    
    # Parameters to limit the number of posts and disable following redirects
    params = {
        'limit': 10
    }
    
    # Make the request to the Reddit API
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    
    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        # If not a valid subreddit, print None
        print(None)

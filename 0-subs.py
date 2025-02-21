#!/usr/bin/python3
"""
This module contains a function to get the number of subscribers
for a given subreddit using the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/your_username)'}

    # Send a GET request to the subreddit about endpoint
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        # Return the number of subscribers
        return data['data']['subscribers']
    else:
        # If not a valid subreddit, return 0
        return 0


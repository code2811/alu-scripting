#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API
and returns titles of all hot articles for a given subreddit.

Functions:
    recurse(subreddit, hot_list=[]): Returns list of all hot article titles
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to get titles of all hot articles
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query
        hot_list (list): List to store article titles (default: None)
        after (str): Token for pagination (default: None)

    Returns:
        list: List of all hot article titles if successful, None if not
    """
    # Initialize hot_list on first call
    if hot_list is None:
        hot_list = []

    # Build the URL for the subreddit's hot posts JSON endpoint
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set custom User-Agent to avoid rate limiting
    headers = {
        "User-Agent": "linux:recursive_hot_posts:v1.0 (by /u/your_username)"
    }

    # Parameters for the request
    params = {
        "limit": 100  # Maximum allowed by Reddit API
    }
    if after:
        params["after"] = after

    try:
        # Make GET request to Reddit API
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Return None for invalid subreddits
        if response.status_code != 200:
            return None

        # Parse the response
        data = response.json()
        posts = data["data"]["children"]
        
        # Add post titles to hot_list
        for post in posts:
            hot_list.append(post["data"]["title"])

        # Get the 'after' token for next page
        after = data["data"]["after"]

        # Base case: no more pages to fetch
        if after is None:
            return hot_list

        # Recursive case: fetch next page
        return recurse(subreddit, hot_list, after)

    except Exception:
        return None

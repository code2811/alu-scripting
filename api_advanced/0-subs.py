#!/usr/bin/python3
"""Module to query Reddit API and get number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    # Reddit API URL
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'linux:subscriber_counter:v1.0 (by /u/your_username)'
    }

    try:
        # Make GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if request was successful and subreddit exists
        if response.status_code == 200:
            # Parse JSON response and extract subscribers count
            data = response.json()
            return data['data']['subscribers']
        else:
            # Return 0 for invalid subreddits or other errors
            return 0

    except Exception:
        # Return 0 if any error occurs
        return 0

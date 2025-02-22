#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit.

Functions:
    number_of_subscribers(subreddit): Returns subscriber count for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        int: The number of subscribers if the subreddit exists,
             0 if the subreddit does not exist or if an error occurs
    """
    # Build the URL for the subreddit's about.json endpoint
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent to avoid rate limiting
    headers = {
        "User-Agent": "linux:subscriber_counter:v1.0 (by /u/your_username)"
    }

    try:
        # Make GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if request was successful and subreddit exists
        if response.status_code == 200:
            # Parse JSON response and extract subscribers count
            data = response.json()
            return data["data"]["subscribers"]
        else:
            # Return 0 for invalid subreddits or other errors
            return 0

    except Exception:
        # Return 0 if any error occurs
        return 0

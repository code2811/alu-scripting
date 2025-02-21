#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and get the
number of subscribers for a given subreddit.

It returns the number of subscribers for a valid subreddit and 0
for an invalid subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers to a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the
        subreddit is invalid or does not exist.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/your_username)'}

    # Send a GET request to the Reddit API about endpoint for the subreddit
    response = requests.get(url, headers=headers)

    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        # Return the number of subscribers
        return data['data']['subscribers']
    else:
        # Return 0 if subreddit does not exist or is invalid
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        if subscribers == 0:
            print(f"Subreddit '{subreddit}' does not exist or is invalid.")
        else:
            print(f"Subreddit '{subreddit}' has {subscribers} subscribers.")


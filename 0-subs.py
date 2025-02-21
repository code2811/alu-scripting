#!/usr/bin/python3
"""
This module queries the Reddit API to retrieve the number of subscribers
for a given subreddit. If the subreddit is valid, it returns the number
of subscribers, otherwise, it returns 0 and prints a message indicating
the subreddit is invalid.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to retrieve the number of subscribers of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit exists, or 0 if it
        does not exist.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/your_username)'}

    # Send GET request to Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status is OK (200)
    if response.status_code == 200:
        data = response.json()
        # Return the number of subscribers
        return data['data']['subscribers']
    else:
        # If subreddit does not exist, return 0
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        if subscribers == 0:
            print(f"Subreddit '{subreddit}' does not exist or is invalid.")
        else:
            print(f"Subreddit '{subreddit}' has {subscribers} subscribers.")


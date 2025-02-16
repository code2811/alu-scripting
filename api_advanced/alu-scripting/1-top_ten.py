#!/usr/bin/python3
"""
Module that provides functionality to interact with the Reddit API
and retrieve the top 10 hot posts for a given subreddit.
This module contains the top_ten function which prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None. Prints either the titles of the hot posts or None if the
        subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'python:alx.api.advanced:v1.0.0 (by /u/alx_student)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)

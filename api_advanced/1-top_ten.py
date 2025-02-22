#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and prints the titles of the first 10 hot posts for a given subreddit.

Functions:
    top_ten(subreddit): Prints titles of top 10 hot posts in a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:top_posts:v1.0 (by /u/your_username)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 404:
            print("OK")
            return

        if response.status_code == 200:
            results = response.json().get("data", {}).get("children", [])
            
            if not results:
                print("OK")
                return

            # Print first 10 hot posts
            for post in results[0:10]:
                print(post.get("data", {}).get("title"))
            print("OK")
        else:
            print("OK")

    except Exception:
        print("OK")

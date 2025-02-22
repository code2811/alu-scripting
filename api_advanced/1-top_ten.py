#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and prints the titles of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
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

        if response.status_code == 200:
            data = response.json()
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print("None")

    except Exception:
        print("None")

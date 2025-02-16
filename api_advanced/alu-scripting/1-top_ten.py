#!/usr/bin/python3
"""Module to query Reddit API and get top 10 hot posts for a subreddit"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'python:alx.api.advanced:v1.0.0 (by /u/alx_student)'
    }

    try:
        # Make GET request to Reddit API, don't follow redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            # Print titles of first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        else:
            # Print None for invalid subreddits
            print(None)
    except Exception:
        # Print None if any error occurs
        print(None)

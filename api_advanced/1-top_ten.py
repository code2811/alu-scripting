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
        None: Prints the titles directly, or prints None for invalid subreddits
    """
    # Build the URL for the subreddit's hot posts JSON endpoint
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent to avoid rate limiting
    headers = {
        "User-Agent": "linux:top_posts:v1.0 (by /u/your_username)"
    }

    # Parameters to limit the response to 10 posts
    params = {
        "limit": 10
    }

    try:
        # Make GET request to Reddit API
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Check if request was successful and subreddit exists
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            posts = data["data"]["children"]

            # Print titles of first 10 posts
            for post in posts:
                print(post["data"]["title"])
        else:
            # Print None for invalid subreddits
            print(None)

    except Exception:
        # Print None if any error occurs
        print(None)

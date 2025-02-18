#!/usr/bin/python3
"""
Module to query Reddit API and recursively count keywords in hot article titles.
"""

import requests
import re


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Queries the Reddit API to get the titles of hot articles and count occurrences of keywords.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of words to count.
        after (str): The 'after' value used for pagination (default is None).
        word_count (dict): Dictionary to store the count of each keyword.

    Returns:
        None: Prints the word count sorted by frequency and alphabetically.
    """
    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}  # Initialize word count

    # Define the Reddit API URL to fetch hot articles
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}" if after else f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set the custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'python:subreddit.keyword.count:v1.0 (by /u/yourusername)'}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the subreddit exists by verifying the status code
        if response.status_code == 404:
            return

        # Parse the JSON response
        data = response.json()
        p


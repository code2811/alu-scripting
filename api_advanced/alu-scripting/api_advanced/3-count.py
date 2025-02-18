#!/usr/bin/python3
"""
Module to query Reddit API and recursively count keywords in hot article titles.
"""

import re
import requests


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
        posts = data['data']['children']

        # Process the titles of each post
        for post in posts:
            title = post['data']['title'].lower()  # Convert title to lowercase

            # Count occurrences of each word in the title
            for word in word_list:
                # Using a regex to match words while ignoring punctuation
                word_pattern = r'\b' + re.escape(word.lower()) + r'\b'
                word_count[word.lower()] += len(re.findall(word_pattern, title))

        # If there are more posts, make a recursive call to fetch the next page of posts
        after = data['data'].get('after', None)
        if after:
            count_words(subreddit, word_list, after, word_count)

        # Once all posts have been processed, print the results
        if after is None:
            # Sort by count (descending) and alphabetically (ascending) in case of tie
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_words:
                if count > 0:  # Only print words that have non-zero count
                    print(f"{word}: {count}")

    except Exception:
        # Handle any exceptions (e.g., network issues) and return nothing
        return


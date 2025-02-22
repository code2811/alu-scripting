#!/usr/bin/python3
"""
Module for counting keyword occurrences in Reddit post titles
using recursive API calls.
"""
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively queries Reddit API and counts occurrences of keywords
    in post titles.

    Args:
        subreddit (str): Subreddit to search
        word_list (list): Keywords to count
        after (str): Token for pagination
        word_counts (dict): Dictionary to store word counts

    Returns:
        None: Prints results directly
    """
    # Initialize word_counts on first call
    if word_counts is None:
        # Convert word list to lowercase and create counter dictionary
        word_counts = {}
        for word in word_list:
            word_lower = word.lower()
            if word_lower in word_counts:
                continue
            word_counts[word_lower] = 0

    # Set up the API request
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:word_counter:v1.0 (by /u/your_username)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Return if subreddit is invalid
        if response.status_code != 200:
            return

        # Parse the response
        data = response.json()
        posts = data["data"]["children"]

        # Process each post title
        for post in posts:
            title_words = post["data"]["title"].lower().split()

            # Count occurrences of each keyword
            for word in title_words:
                # Check if word matches any keyword exactly
                if word in word_counts:
                    word_counts[word] += 1

        # Get the after token for next page
        after = data["data"]["after"]

        # Base case: no more pages
        if after is None:
            # Sort and print results
            sorted_counts = sorted(
                word_counts.items(),
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_counts:
                if count > 0:
                    print("{}: {}".format(word, count))
            return

        # Recursive case: fetch next page
        return count_words(subreddit, word_list, after, word_counts)

    except Exception:
        return

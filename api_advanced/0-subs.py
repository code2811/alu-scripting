
dule to query Reddit API and get subscriber count for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'python:alx.api.advanced:v1.0.0 (by /u/alx_student)'
    }

    try:
        # Make GET request to Reddit API, don't follow redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if request was successful and return subscriber count
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # Return 0 for invalid subreddits or other errors
            return 0
    except Exception:
        # Return 0 if any error occurs during the request

        return 0i

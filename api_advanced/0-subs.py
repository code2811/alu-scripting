#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    # Define the base URL and headers for the request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'myAPI/0.1'}

    # Send a GET request to the subreddit about page
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and get the subscriber count
        data = response.json()
        return data['data']['subscribers']
    else:
        # If the subreddit is invalid or there's an error, return 0
        return 0


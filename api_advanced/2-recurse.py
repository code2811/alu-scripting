#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[]):
    # Define the URL and headers for the request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'myAPI/0.1'}
    
    # Send a GET request to the subreddit hot page
    response = requests.get(url, headers=headers, params={'after': None})

    # Check if the response status is valid (200 OK)
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json()

    # Get the list of hot posts and append their titles to hot_list
    for post in data['data']['children']:
        hot_list.append(post['data']['title'])

    # Check if there is more data (pagination)
    after = data['data'].get('after')
    if after:
        # If there is more data, recurse with the next page
        return recurse(subreddit, hot_list)
    
    # Base case: Return the final list when no more pages are available
    return hot_list


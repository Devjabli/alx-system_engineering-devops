#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "subreddit-subscriber-counter/0.1"}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=20)

        # Check if the response was successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the subreddit is not found or any other issue occurs, return 0
            return 0
    except requests.RequestException:
        # If there was an issue with the request, return 0
        return 0

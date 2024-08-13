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
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=20)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        return 0

    except requests.RequestException:
        return 0

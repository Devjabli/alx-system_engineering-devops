#!/usr/bin/python3
"""
Function to query the Reddit API and print the titles
of the first 10 hot posts for a specific subreddit.
"""

import requests

def print_top_ten_posts(subreddit):
    """
    Queries the Reddit API to print the titles of the first 10 hot posts
    for a given subreddit. If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title", "No title available")
            print(title)
    else:
        print(None)

#!/usr/bin/python3
"""
Function to count the occurrence of specified words in all hot posts of a given Reddit subreddit.
"""
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function that queries the Reddit API, processes the titles of all
    hot posts, and prints a sorted count of specified keywords.
    """
    if not word_list or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False, timeout=30
    )

    if response.status_code != 200:
        return

    posts = response.json().get("data", {}).get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title:
                counts[word] = counts.get(word, 0) + title.count(word_lower)

    after = response.json().get("data", {}).get("after", None)
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")

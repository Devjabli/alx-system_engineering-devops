#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            return 0
    except requests.RequestException:
        return 0
    
    return 0

# Test cases
if __name__ == "__main__":
    print(number_of_subscribers('programming'))  # Expected: (actual subscriber count)
    print(number_of_subscribers('this_is_a_fake_subreddit'))  # Expected: 0

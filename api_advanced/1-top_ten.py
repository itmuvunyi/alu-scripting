#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    # Prevent redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")
    if not data or not data.get("children"):
        print(None)
        return

    for post in data.get("children"):
        print(post.get("data").get("title"))

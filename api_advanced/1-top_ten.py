#!/usr/bin/python3
"""
Module to query the Reddit API and print the top 10 hot post titles
from a specified subreddit.

Functions:
    top_ten(subreddit): Prints top 10 hot post titles from subreddit.
"""

import requests


def top_ten(subreddit):
    """Fetches and prints the titles of the top ten hot posts from a subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'Python:RedditTopTen:v1.0 (by /u/test-script)',
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if not response.ok:
        print(None)
        return

    try:
        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))

    except (ValueError, KeyError):
        print(None)

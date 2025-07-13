#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    Prints None if the subreddit is invalid.
    """
    if not isinstance(subreddit, str) or not subreddit:
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "python:hot.posts.viewer:v1.0 (by /u/anonymous_dev_script)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {}).get("children", [])

        for post in data:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except requests.RequestException:
        print("None")

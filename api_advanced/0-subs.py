#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a subreddit.
If the subreddit is invalid, returns 0.
"""
import requests


def number_of_subscribers(subreddit):
    if not isinstance(subreddit, str) or subreddit == "":
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "MyRedditAPI/0.1"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except Exception:
        return 0

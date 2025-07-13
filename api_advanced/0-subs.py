#!/usr/bin/python3
"""
This module defines a function that queries the Reddit API
and returns the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:subreddit.subscriber.counter:v1.0 "
                      "(by /u/anonymous_dev_script)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        return 0
    except requests.RequestException:
        return 0

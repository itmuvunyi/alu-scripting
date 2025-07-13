#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns the total number of subscribers
    for the given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:alu.scripting:v1.0 (by /u/anonymous_dev_script)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0

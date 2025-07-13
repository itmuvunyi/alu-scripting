#!/usr/bin/python3
"""
Recursive function to query the Reddit API and return a list of hot post titles.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches all hot post titles for a given subreddit.

    Args:
        subreddit (str): Subreddit name
        hot_list (list): Accumulator list for hot post titles
        after (str): Token for next page

    Returns:
        list: Titles of hot posts, or None if subreddit is invalid
    """
    if not isinstance(subreddit, str) or not subreddit:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "python:recurse.hot.posts:v1.0 (by /u/anonymous_dev_script)"
    }
    params = {
        "limit": 100,
        "after": after
    }

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        # Recursive case: keep going if there's a next page
        next_after = data.get("after")
        if next_after is not None:
            return recurse(subreddit, hot_list, next_after)
        else:
            return hot_list

    except requests.RequestException:
        return None

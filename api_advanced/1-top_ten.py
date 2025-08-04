#!/usr/bin/python3
"""
Function that queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Python:top.ten:v1.0 (by /u/fakeuser)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")

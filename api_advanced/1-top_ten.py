#!/usr/bin/python3 
"""
A function that queries the Reddit API and prints the titles.
"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'script:reddit.title.fetcher:v1.0 (by /u/yourusername)',
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch data:", response.status_code)
        print(None)
        return

    try:
        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            print("No posts found.")
            print(None)
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except ValueError:
        print("Error parsing JSON.")
        print(None)

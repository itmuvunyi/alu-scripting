#!/usr/bin/python3
"""
Function that queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyRedditApp/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    try:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    except Exception:
        print(None)

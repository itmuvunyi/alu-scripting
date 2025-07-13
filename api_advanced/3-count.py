#!/usr/bin/python3
"""
Recursive function to query Reddit API, parse hot post titles,
and count given keywords (case-insensitive, space-delimited).
"""

import requests
import re


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Prints a sorted count of given keywords in subreddit hot article titles.
    """
    if word_count is None:
        # Initialize word counts (all lowercase, combined if repeated)
        word_count = {}
        for word in word_list:
            lw = word.lower()
            word_count[lw] = word_count.get(lw, 0)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "python:keyword.counter:v1.0 (by /u/anonymous_dev_script)"
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
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            words = re.findall(r'\b\w+\b', title)

            for word in words:
                if word in word_count:
                    word_count[word] += 1

        # Recurse if there's a next page
        next_after = data.get("after")
        if next_after is not None:
            return count_words(subreddit, word_list, next_after, word_count)

        # All recursion is done: now sort & print results
        filtered = {k: v for k, v in word_count.items() if v > 0}
        sorted_result = sorted(
            filtered.items(),
            key=lambda item: (-item[1], item[0])
        )
        for word, count in sorted_result:
            print(f"{word}: {count}")

    except requests.RequestException:
        return

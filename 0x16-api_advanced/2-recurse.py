#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing
the titles of all hot articles
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    # If hot_list is not provided, initialize it to an empty list
    if hot_list is None:
        hot_list = []

    # Set the Default URL strings
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)

    # Set an User-Agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Set the Query Strings to Request
    payload = {'after': after, 'limit': '100'}

    # Get the Response of the Reddit API
    res = requests.get(api_uri, headers=user_agent,
                       params=payload, allow_redirects=False)

    # Check if the subreddit is invalid
    if res.status_code == 200:
        res = res.json()
        hot_posts = res.get('data').get('children')

        # Add each hot post title to the list
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))

        # Get the next page of hot posts
        after = res.get('data').get('after')
        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    # If the subreddit is invalid, return None
    return None

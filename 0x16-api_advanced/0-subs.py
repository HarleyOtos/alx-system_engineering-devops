#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit: A string representing the name of the subreddit.

    Returns:
        The number of subscribers for the given subreddit,
        or 0 if the subreddit is invalid.
    """
    # Construct the API endpoint URL for the given subreddit
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent header to avoid API request errors
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # Make an API request to the endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit exists and has a valid response status code
    if response.status_code == 200:
        # Extract the number of subscribers from the response JSON data
        data = response.json().get('data', {})
        return data.get('subscribers', 0)

    # The subreddit is invalid, so return 0
    return 0

#!/usr/bin/python3
"""
Queries the Reddit API and prints a sorted count of given keywords.
"""
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Queries the Reddit API recursively and prints
    a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit to search in.
        word_list (list): A list of keywords to search for.
           Case-insensitive, delimited by spaces.
        after (str, optional): The "after" parameter for the API request.
        counts (dict, optional): A dictionary to store the count of
            each keyword. Defaults to an empty dictionary.

    Returns:
        None: Prints the sorted count of keywords.

    Note:
        If word_list contains the same word (case-insensitive),
        the final count should be the sum of each duplicate.
        Results should be printed in descending order,
        by the count. If the count is the same for separate keywords,
        they should then be sorted alphabetically (ascending, from A to Z).
        Words with no matches should be skipped and
        not printed. Words must be printed in lowercase.
    """
    if after == "STOP":
        # Base case: we've processed all the pages
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return

    data = response.json()
    articles = data.get("data", {}).get("children", [])
    for article in articles:
        title = article.get("data", {}).get("title", "").lower()
        for word in word_list:
            if title.count(word) > 0:
                counts[word] = counts.get(word, 0) + title.count(word)

    after = data.get("data", {}).get("after")
    count_words(subreddit, word_list, after, counts)

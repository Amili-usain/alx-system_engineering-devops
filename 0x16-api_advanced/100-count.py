#!/usr/bin/python3
""" request the top ten hot posts """
import requests


def count_words(subreddit, word_list, afters="", before="", count={}):
    """ function to get top hot posts
    Args:
    subreddit (string): subreddit queried
"""
    web = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, afters)
    headers = {'User-Agent': 'MyAPI/0.1'}
    main = requests.get(web,
                        headers=headers, allow_redirects=False)
    before = main.json()['data']['before']
    if (main.json().get('error') == 404):
        return None
    if (before is None and afters is None):
        for C in word_list:
            for post in main.json()['data']['children']:
                hold = [x.lower() for x in post['data']['title'].split()]
                if C in hold:
                    if count.get(C) is None:
                        count[C] = 0
                    count[C] += hold.count(C.lower())
        for words, numbers in count.items():
            print("{}: {}".format(words, numbers))
    elif (afters is not None):
        afters = main.json()['data']['after']
        for C in word_list:
            for post in main.json()['data']['children']:
                hold = [x.lower() for x in post['data']['title'].split()]
                if C in hold:
                    if count.get(C) is None:
                        count[C] = 0
                    count[C] += hold.count(C.lower())
        count_words(subreddit, word_list, afters, count)
    else:
        for words, numbers in count.items():
            print("{}: {}".format(words, numbers))

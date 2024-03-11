#!/usr/bin/python3
"""
A python script querying the reddit api
"""
import requests
import sys


def number_of_subscribers(subreddit):
    r = requests.get('https://reddit.com/r/programming/about', allow_redirects=False)

    print(r.__dict__)


if __name__ == '__main__':
    subreddit = sys.argv[1]
    print(number_of_subscribers(subreddit))

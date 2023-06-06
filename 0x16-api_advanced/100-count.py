#!/usr/bin/python3
""" raddit api"""

import requests
import re

def count_words(subreddit, word_list):
  """
  Recursively queries the Reddit API for hot articles in the given subreddit, parses the titles of the articles, and prints a sorted count of the given keywords.

  Args:
    subreddit: The name of the subreddit to query.
    word_list: A list of keywords to search for.

  Returns:
    A dictionary that maps each keyword to the number of times it appears in the hot articles of the given subreddit.
  """

  if not subreddit or not word_list:
    return {}

  # Make a request to the Reddit API to get the hot articles in the given subreddit.
  response = requests.get('https://api.reddit.com/r/{}/hot.json'.format(subreddit))
  if response.status_code != 200:
    return {}

  # Parse the titles of the hot articles.
  articles = response.json()['data']['children']
  titles = [article['data']['title'] for article in articles]

  # Count the number of times each keyword appears in the titles.
  counts = {}
  for word in word_list:
    word = word.lower()
    counts[word] = titles.count(word)

  # Sort the counts by value, in descending order.
  sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

  # Print the sorted counts.
  for keyword, count in sorted_counts:
    print('{}: {}'.format(keyword, count))

  # Recursively call the function to count the words in the hot articles of any child subreddits.
  for subreddit in articles[0]['data']['subreddits']:
    counts.update(count_words(subreddit, word_list))

  return counts

if __name__ == '__main__':
  if len(sys.argv) < 3:
    print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
    print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
  else:
    result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])

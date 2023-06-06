#!/usr/bin/python3
""" raddit api"""
import requests

def count_words(subreddit, word_list, count={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        articles = data["data"]["children"]

        for article in articles:
            title = article["data"]["title"].lower()
            for word in word_list:
                word = word.lower()
                if word not in count:
                    count[word] = 0
                count[word] += title.count(f" {word} ")

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, count)

    sorted_counts = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")


# Example usage
count_words("programming", ["react", "python", "java", "javascript", "scala", "no_results_for_this_one"])


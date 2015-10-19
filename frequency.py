__author__ = 'sridhar'

import json
import re


def load_tweet_parse(file):
    tweets_text_parsed = []
    tweets_text = []
    for line in file:
        try:
            loaded_tweet = json.loads(line)
            tweets_text.append(loaded_tweet['text'])
        except:
            continue

    pattern = re.compile(r'\w+')
    for text in tweets_text:
        tweets_text_parsed.append(pattern.findall(text))

    return tweets_text_parsed


def hw(tweet_file):
    parsed = load_tweet_parse(tweet_file)
    dic = {}
    for list_word in parsed:
        for word in list_word:
            dic[word] = dic.get(word) + 1 if word in dic else 1
    print dic


def main():
    # tweet_file = open(sys.argv[2])
    tweet_file = open('output.txt')
    hw(tweet_file)

if __name__ == '__main__':
    main()

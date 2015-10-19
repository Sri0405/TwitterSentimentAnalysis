__author__ = 'sridhar'

"""
    Calculate the sentiment score of Tweet by parsing the tweet and computing the sentiment value of each term
    using the term sentiment dictionary

    Get the list of tweets using a Twitter Stream Crawler

    Introduction to DataScience Course - University of Washington

"""

import sys
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


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}  # initialize an empty dictionary

    """ define scores dictionary """

    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    parsed = []
    parsed = load_tweet_parse(tweet_file)

    tweet_word_scores=[]
    final_scores =[]
    # print parsed[10]
    """ calcuate score of tweet """
    for wlist in parsed:
        tweet_scores = [scores.get(word,0) for word in wlist]
        final_scores.append(sum(tweet_scores))
        # print parsed

    print final_scores[1:10]
    
if __name__ == '__main__':
    main()

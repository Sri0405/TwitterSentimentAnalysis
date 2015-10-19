import sys
import json
import re


def getDict(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    return scores


def hw(sent_file, tweet_file):
    dictionary_scores = getDict(sent_file)
    parsed_tweets = load_tweet_parse(tweet_file)

    newterms = {}

    for tweet in parsed_tweets:

        positives = 0
        negatives = 0
        local_new = []

        for word in tweet:
            value = dictionary_scores.get(word, 0)
            if value > 0:
                positives = positives + 1
            elif value < 0:
                negatives = negatives + 1
            else:
                local_new.append(word)

        val = float(positives) / \
            float(negatives) if negatives is not 0 else positives

        for t in local_new:
            newterms[t] = newterms[t] + val if t in newterms else val

    for key, val in newterms.items():
        print key, val


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
    hw(sent_file, tweet_file)


if __name__ == '__main__':
    main()

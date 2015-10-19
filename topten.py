# author - sridhar
import sys
import json


def load_tweet_text(tweet_file):
    tweets_text = []
    for line in tweet_file:
        try:
            loaded_tweet = json.loads(line)
            tweets_text.append(loaded_tweet)
        except:
            continue
    return tweets_text


def main():
    tweet_file = open(sys.argv[1])
    tweets_text = load_tweet_text(tweet_file)

    dict_terms = {}
    for parts in tweets_text:
        lookup = parts.get('entities')
        if lookup is not None:
            tag = lookup.get('hashtags')
            for vals in tag:
                if vals is not None:
                    val = vals.get('text')
                    if val is not None:
                        dict_terms[val] = 1 if not val in dict_terms else dict_terms[
                            val] + 1

    sorted_dict = sorted(
        dict_terms.items(), key=lambda term: term[1], reverse=True)
    for key, val in sorted_dict[0:10]:
        print key, val

if __name__ == "__main__":
    main()

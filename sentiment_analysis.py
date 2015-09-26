from __future__ import division
import urllib
import csv
from string import punctuation

#Function to read the tweet file
def tweet_set(filename):
    tweets = open(filename).read()
    tweets_list = tweets.split('\n')
    return tweets_list

#Function to read the sentiment files
def word_set(filename):
    words_array = open(filename).read()
    word_list=words_array.split('\n')
    return word_list

#Function to perform the sentiment analysis
def tweet_analysis():
    # List to store Analysis
    positive_counts = []    #To store the count for positive words in a tweet
    negative_counts = []    #To store the count for negative words in a tweet
    word_counter = []       #To get total number of words ina tweet
    char_counter = []       #To get total number of characters in a tweet
    pos_lex_div = []        #Lexical Diversity Calculation [No. of +ve words in a tweet/ total +ve words]
    neg_lex_div = []        #Lexical Diversity Calculation [No. of -ve words in a tweet/ total -ve words]
    lexical_diversity = []

    #Get list of tweets from file
    tweets_list = tweet_set("posTweets.txt")

    #Get list of positive words from file
    positive_words = word_set("pos.wn")

    #Get list of negative words from file
    negative_words = word_set("neg.wn")

    #The tweet analysis loop starts
    for tweet in tweets_list:
        positive_counter = 0
        negative_counter = 0

        #Pre-processing the tweets
        #_convert the tweets to lowercase
        tweet_processed = tweet.lower()

        #Calculating Lexical Diversity

        if len(tweet_processed) != 0:
            lexical_diversity.append(100 * (len(set(tweet_processed))/len(tweet_processed)))
        else:
            lexical_diversity.append(0)

        #print lexical_diversity
        #Calculating Character Count
        char_counter.append(len(tweet_processed))

        #_Remove all punctuations from the tweet
        for p in list(punctuation):
            tweet_processed = tweet_processed.replace(p, '')

        #splitting the words in tweet
        words = tweet_processed.split(' ')
        word_count = len(words)

        #Add the words counter for each tweet
        word_counter.append(word_count)

        #Calucilating the number of +ve/-Ve words in the tweet
        for word in words:
            if word in positive_words:
                positive_counter = positive_counter + 1
            elif word in negative_words:
                negative_counter = negative_counter + 1

        #counting the number of positive words
        positive_counts.append(positive_counter)

        #counting the number of positive words
        negative_counts.append(negative_counter)

    #Collecting all the caluclation for the analysis and writing it to a CSV file
    output=zip(tweets_list,positive_counts,negative_counts,lexical_diversity, word_counter, char_counter)

    #Write to CSV file
    o_file = open('tweet_sentiment_analysis.csv', 'wb')
    writer = csv.writer(o_file)
    writer.writerows(output)
    #Always close the file
    o_file.close()

    #The tweet analysis loop ends

tweet_analysis()
#The code ends here

#
# ECE 143 Group Project
#
# Simple script that counts the occurance frequencies of
# the words in a specific file.
#
# by Renjie Zhu on Oct 24, 2018
#
# modified: 
#   Daoyu: PoS analysis
#   Ambareesh: bigram implementation
#

import nltk
from collections import Counter

# Download nltk resources
nltk.download('averaged_perceptron_tagger')
nltk.download("wordnet")

# keeping track of a common words list, this is a list of words that we
# don't want in our data.
# List saved as common_words.txt
common_words = []
with open('common_words.txt','rt') as f:
    for line in f.readlines():
        common_words.append(line.strip('\n'))
common_words.extend(list(map(chr, range(97, 123))))

def word_freq(file_name):
    """
    word_freq

    arguments
    --------

    filename : filename of the raw data
        type: string

    return
    ------

    single_frequency
        type: dictionary

    bigram_frequency
        type: dictionary
    """
    with open(file_name, 'r',encoding='utf-8',errors='ignore') as f:
        lines = f.read()

    # Get rid of unwanted chars and splitting the string into a list of words
    origlist = lines.lower().split()
    wordlist = [i.strip(".:,();$-1234567890") for i in origlist]
    # wordfreq = [wordlist.count(j) for j in wordlist]
    # freqdict = dict(zip(wordlist, wordfreq))
    freqdict = dict(Counter(wordlist))
    newfreq = {}
    for key, value in freqdict.items():
        
        if key in common_words:
            continue
        else:
            newfreq[key] = value


    posFreq = nltk.pos_tag(list(newfreq.keys()))
    # Convert the list created by nltk to dict
    posDict = {word: pos for word, pos in posFreq}

    # Count only Noun words
    lemmatizer = nltk.WordNetLemmatizer()
    single_frequency = {}
    for key, value in newfreq.items():
        if posDict[key] == 'NN' or posDict[key] == 'NNS':
            key = lemmatizer.lemmatize(key)
            if key in single_frequency.keys():
                single_frequency[key] = single_frequency[key] + value
            else:
                single_frequency[key] = value

    # bigrams
    # bigrams make two word combos of all space separated words,
    # bigram_list = [ ('circuit','anlaysis'), ('analysis','problem'), ('problem', 'from')..]
    bigram_list = list(nltk.bigrams(wordlist))
    freq_bigram = dict(Counter(bigram_list))

    bigram_frequency = {}
    for key, value in freq_bigram.items():
        if value < 2:
            continue
        elif key[0] in common_words or key[1] in common_words:
            continue
        # elif not (key[0] in posDict.keys() and key[1] in posDict.keys()):
        #     continue
        elif posDict[key[0]] == 'NN' or posDict[key[0]] == 'NNS' or posDict[key[0]] == 'JJ':
            if posDict[key[1]] == 'NN' or posDict[key[1]] == 'NNS':
                bigram_frequency[key[0] + ' ' + key[1]] = value

    return single_frequency, bigram_frequency
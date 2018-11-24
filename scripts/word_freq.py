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
import os
from collections import Counter
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Download nltk resources
nltk.download('averaged_perceptron_tagger')
nltk.download("wordnet")

# keeping track of a common words list, this is a list of words that we
# don't want in our data.
# List saved in common_words.txt
common_words = []
with open(os.path.join('scripts','common_words.txt'), 'rt') as f:
    for line in f.readlines():
        common_words.append(line.strip('\n'))
common_words.extend(list(map(chr, range(97, 123))))

logger.info(f'"common_words.txt" loaded.')
# print("[word_freq] 'common_words.txt' loaded.")


def word_freq(file_name):
    """
    word_freq counts the words and bigrams in the file
    returning two dictionaries containing all the words with
    their corresponding frequencies and same for bigrams.

    Bigram: a pair of consecutive written units

    We believe, during discussions and further confirmed, that
    bigram frequency lists gives us more information about the 
    file.

    arguments
    --------

    filename : filename of the raw data
        type: string

    return
    ------

    single_frequency
        type: dictionary
        key: words (type: string)
        value: their corresponding frequencies (type: integer)

    bigram_frequency
        type: dictionary
        key: bigram phrases (type: string)
        value: their corresponding frequencies (type: integer)

    """
    assert isinstance(file_name, str)

    # opening the file with correct encoding and read them into memory
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.read()

    # Get rid of unwanted chars and splitting the string into a list of words
    orig_list = lines.lower().split()
    word_list = [i.strip(".:,();$-1234567890") for i in orig_list]

    # count the frequencies of words in the word_list
    # and pack this returnning list of tuples in to a dictionary
    freq_dict = dict(Counter(word_list))

    # getting rid of all the common words that we don't want
    # putting all of the remaining words into a new dictionary
    needed_freq = {}
    for key, value in freq_dict.items():
        if key in common_words:
            continue
        else:
            needed_freq[key] = value

    # use *natural language tool kit* (nltk) to analyze the part of speech (pos)
    # of the words. We pay more attention to nouns which will give the most information
    # and conjunctions and pronouns.
    pos_freq = nltk.pos_tag(list(needed_freq.keys()))
    # Convert the list created by nltk to dict
    pos_dict = {word: pos for word, pos in pos_freq}

    # *note*: we realized that we should probably do nltk pos analysis first as
    # it would already help us eliminate a lot of the unwanted words, such as, 'the', 'a',
    # and so on. We did the other way because the the original dictionary was too large to
    # pass through the nltk.pos_tag().

    # Count only Noun words and this results in our final single word frequency dictionary
    lemmatizer = nltk.WordNetLemmatizer()
    single_frequency = {}
    for key, value in needed_freq.items():
        if pos_dict[key] == 'NN' or pos_dict[key] == 'NNS':
            key = lemmatizer.lemmatize(key)
            if key in single_frequency.keys():
                single_frequency[key] = single_frequency[key] + value
            else:
                single_frequency[key] = value

    # bigrams
    # bigrams make two word combos of all space separated words,
    # bigram_list = [ ('circuit','anlaysis'), ('analysis','problem'), ('problem', 'from')..]
    bigram_list = list(nltk.bigrams(word_list))
    bigram_freq_temp = dict(Counter(bigram_list))
    bigram_frequency = {}
    for key, value in bigram_freq_temp.items():
        if key[0] in common_words or key[1] in common_words:
            continue
        # elif not (key[0] in posDict.keys() and key[1] in posDict.keys()):
        #     continue
        elif pos_dict[key[0]] == 'NN' or pos_dict[key[0]] == 'NNS' or pos_dict[key[0]] == 'JJ' or pos_dict[key[0]] == 'VBN' or pos_dict[key[0]] == 'VBP' or pos_dict[key[0]] == 'VBD':
            if pos_dict[key[1]] == 'NN' or pos_dict[key[1]] == 'NNS' or pos_dict[key[1]] == 'VBG' or pos_dict[key[1]] == 'VBZ' or pos_dict[key[1]] == 'VBD' or pos_dict[key[1]] == 'JJ':
                if key[0] + ' ' + key[1] in common_words:
                    continue
                bigram_frequency[key[0] + ' ' + key[1]] = value

    return single_frequency, bigram_frequency

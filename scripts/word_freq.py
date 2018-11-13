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

# be careful of the location of this file, if moved, be sure to rethink about the file paths

import os
import nltk
from collections import Counter
# import apsw_script
from SQLite import SQLite

# Download nltk resources
nltk.download('averaged_perceptron_tagger')
nltk.download("wordnet")

# parent dir for mac or linux
parent_dir = os.getcwd()
# parent dir for windows machine (uncomment if on windows, leave commented if elsewise)
parent_dir = os.path.dirname(parent_dir)
# os.path.join joins all the arguments given in the function call
file_data = os.path.join(parent_dir, 'raw_data', input(
    'What is the data file name? (Make sure the file is in "raw_data" folder, give file name with extension)'))
table_name = input(
    'What is the database table name (convention: school_dept_year) ? ')
table_b = table_name + '_bigram'
table_s = table_name + '_single'
# file_out_b = os.path.join(parent_dir,'processed_data',file_out_b)
# file_out_s = os.path.join(parent_dir,'processed_data',file_out_s)

# keeping track of a common words list, this is a list of words that we
# don't want in our data.
# List saved as common_words.txt
common_words = []
with open('common_words.txt','rt') as f:
    for line in f.readlines():
        common_words.append(line.strip('\n'))
common_words.extend(list(map(chr, range(97, 123))))

with open(file_data, 'r') as f:
    lines = f.read()


# Get rid of unwanted chars and splitting the string into a list of words
origlist = lines.lower().split()
wordlist = [i.strip(".:,();$-1234567890") for i in origlist]
# wordfreq = [wordlist.count(j) for j in wordlist]
# freqdict = dict(zip(wordlist, wordfreq))
freqdict = dict(Counter(wordlist))
newfreq = {}
for key, value in freqdict.items():
    # if value < 3:
    #     continue
    if key in common_words:
        continue
    else:
        newfreq[key] = value


posFreq = nltk.pos_tag(list(newfreq.keys()))
# Convert the list created by nltk to dict
posDict = {word: pos for word, pos in posFreq}

# Count only Noun words
lemmatizer = nltk.WordNetLemmatizer()
nnfreq = {}
for key, value in newfreq.items():
    if posDict[key] == 'NN' or posDict[key] == 'NNS':
        key = lemmatizer.lemmatize(key)
        if key in nnfreq.keys():
            nnfreq[key] = nnfreq[key] + value
        else:
            nnfreq[key] = value

# bigrams
# bigrams make two word combos of all space separated words,
# bigram_list = [ ('circuit','anlaysis'), ('analysis','problem'), ('problem', 'from')..]
bigram_list = list(nltk.bigrams(wordlist))
freq_bigram = dict(Counter(bigram_list))

picked_freq_bigram = {}
for key, value in freq_bigram.items():
    if value < 2:
        continue
    elif key[0] in common_words or key[1] in common_words:
        continue
    # elif not (key[0] in posDict.keys() and key[1] in posDict.keys()):
    #     continue
    elif posDict[key[0]] == 'NN' or posDict[key[0]] == 'NNS' or posDict[key[0]] == 'JJ':
        if posDict[key[1]] == 'NN' or posDict[key[1]] == 'NNS':
            picked_freq_bigram[key[0] + ' ' + key[1]] = value

# with open(file_out_s, 'w') as f:
#     for key, value in reversed(sorted(nnfreq.items(), key=lambda x: x[1])):
#         f.write(f'{key}: {value}\n')

# with open(file_out_b, 'w') as f:
#     for key, value in reversed(sorted(picked_freq_bigram.items(), key=lambda x: x[1])):
#         f.write(f'{key}: {value}\n')

# I am trying to get the data into the database, just testing for now (Renjie)
# # loading data to database
# _, cursor = apsw_script.connect_db('database.db')
# err = apsw_script.create_table(cursor, table_b)
# # probably log this? as 1 means something happened
# err = apsw_script.insert_dict(cursor, table_b, picked_freq_bigram)

# err = apsw_script.create_table(cursor, table_s)
# err = apsw_script.insert_dict(cursor, table_s, nnfreq)

db = SQLite('database.db')
err = db.create_table(table_b)
err = db.insert_dict(table_b, picked_freq_bigram)

err = db.create_table(table_s)
err = db.insert_dict(table_s, nnfreq)
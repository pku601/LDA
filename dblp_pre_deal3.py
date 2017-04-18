# -*- coding: utf-8 -*-
import codecs
import sys
import re
from stemming.porter2 import stem
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer

reload(sys)
sys.setdefaultencoding('utf8')

stop_words = []

lem = WordNetLemmatizer()


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def lemmatize_sentence(sentence):
    res = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(word_tokenize(sentence)):
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))

    return res

with open('StopWordTable.txt', 'r') as f:
    for line in f:
        stop_words.append(line.strip())

fout = open('dblp_titles_clean2.txt', 'wb')

with open('dblp_titles_clean.txt', 'r') as f:
    line_num = 0
    for line in f:
        line_num += 1
        if line_num % 10000 == 0:
            print line_num

        words = line.strip().split(' ')

        # to lower case
        words = [i.lower() for i in words]

        # WordNet Lemmatizer
        sentence = ' '.join(words)
        sentence = lemmatize_sentence(sentence)

        # remove stop words
        sentence = [i for i in sentence if i not in stop_words]

        final_result = ' '.join(sentence)

        fout.write(final_result)
        fout.write('\n')

fout.close()

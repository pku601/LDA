from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import time_util

# input_file = 'dblp_titles_without_titleelement.txt'
input_file = 'small_data_20000.txt'
tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
print time_util.get_current_time()
# change dblp file to a list
doc_set = []
with open(input_file, 'r') as f:
    for line in f:
        doc_set.append(line.strip())
print 'dblp file to list end...'
print time_util.get_current_time()
# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if i not in en_stop]

    # stem token
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    # add tokens to list
    texts.append(stemmed_tokens)
print 'pre deal end...'
print time_util.get_current_time()

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=20)
print(lda_model.print_topics(num_topics=2, num_words=4))
# print example:
# [(0, u'0.030*"fuzzi" + 0.021*"model" + 0.021*"base" + 0.016*"data"'),
# (1, u'0.027*"system" + 0.017*"base" + 0.015*"knowledg" + 0.012*"design"')]

print '...End...'
print time_util.get_current_time()

# Usage:
# python sample_for_dblp.py

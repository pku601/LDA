# -*- coding:utf-8 -*-
# 中文注释
import numpy as np
import lda
import matplotlib.pyplot as plt
import textmining

tdm = textmining.TermDocumentMatrix()
with open('small_data.txt', 'r') as f:
    for line in f:
        tdm.add_doc(line.strip())

# create a temp variable with doc-term info
temp = list(tdm.rows(cutoff=1))

# get the vocab from first row
vocab = tuple(temp[0])

# get document-term matrix from remaining rows
X = np.array(temp[1:])

# X = lda.datasets.load_reuters()
# vocab = lda.datasets.load_reuters_vocab()
# titles = lda.datasets.load_reuters_titles()
print X.shape
print X.sum()

model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))

# doc_topic = model.doc_topic_
# for i in range(10):
#     print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))

# plt.plot(model.loglikelihoods_[5:])

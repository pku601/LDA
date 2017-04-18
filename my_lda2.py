# -*- coding:utf-8 -*-
# 中文注释

import lda
import matplotlib.pyplot as plt

X = lda.datasets.load_reuters()
titles = lda.datasets.load_reuters_titles()
X_train = X[10:]
X_test = X[:10]
titles_test = titles[:10]

model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X_train)
doc_topic_test = model.transform(X_test)
for title, topics in zip(titles_test, doc_topic_test):
    print("{} (top topic: {})".format(title, topics.argmax()))

# plt.plot(model.loglikelihoods_[5:])

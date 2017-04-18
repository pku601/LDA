#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An example of getting titles and vocab for lda using textmine package.

-- adapted from: http://www.christianpeccei.com/textmining/

"""
from __future__ import print_function

import numpy as np
import textmining

# Create some very short sample documents
doc1 = 'John and Bob are brothers.'
doc2 = 'John went to the store. The store was closed.'
doc3 = 'Bob went to the store too.'

print("\n**These are the 'documents', making up our 'corpus':")
for n, doc in enumerate([doc1, doc2, doc3]):
    print("document {}: {}".format(n+1, doc))

print("-- In real applications, these 'documents' "
      "might be read from files, websites, etc.")

# make a titles tuple
# -- these should be the "titles" for the "documents" above
titles = ("Brothers.",
          "John to the store.",
          "Bob to the store.")

print("\n**These are the 'document titles':")
for n, title in enumerate(titles):
    print("title {}: {}".format(n+1, title))

print("-- In real applications, these 'titles' might "
      "be the file name, the story title, webpage title, etc.")

# Initialize class to create term-document matrix
print("\n** The textmining packages is one tool for creating the "
      "'document-term' matrix, 'vocabulary', etc."
      "\n   You can write your own, if needed.")
tdm = textmining.TermDocumentMatrix()

# Add the documents
tdm.add_doc(doc1)
tdm.add_doc(doc2)
tdm.add_doc(doc3)

# create a temp variable with doc-term info
temp = list(tdm.rows(cutoff=1))

# get the vocab from first row
vocab = tuple(temp[0])

# get document-term matrix from remaining rows
X = np.array(temp[1:])

##
## print out info, as in blog post with a little extra info
##
## post: http://bit.ly/1bxob2E
##
print("\n** Output produced by the textmining package...")

# document-term matrix
print("* The 'document-term' matrix")
print("type(X): {}".format(type(X)))
print("shape: {}".format(X.shape))
print("X:", X, sep="\n" )
print("-- Notice there are 3 rows, for 3 'documents' and\n"
      "   12 columns, for 12 'vocabulary' words\n"
      "-- The number of rows and columns depends on the number of documents\n"
      "   and number of unique words in -all- documents")

# the vocab
print("\n* The 'vocabulary':")
print("type(vocab): {}".format(type(vocab)))
print("len(vocab): {}".format(len(vocab)))
print("vocab:", vocab, sep="\n")
print("-- These are the 12 words in the vocabulary\n"
      "-- Often common 'stop' words, like 'and', 'the', 'to', etc are\n"
      "   filtered out -before- creating the document-term matrix and vocab")

# titles for each story
print("\n* Again, the 'titles' for this 'corpus':")
print("type(titles): {}".format(type(titles)))
print("len(titles): {}".format(len(titles)))
print("titles:", titles, sep="\n", end="\n\n")

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer


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

senten = 'Condensing the work of any academic scientist into a one dimensional indicator of scientific performance is a difficult problem Here we employ Bayesian statistics to analyze several different indicators of scientific performance Specifically we determine each indicator s ability to discriminate between scientific authors Using scaling arguments we demonstrate that the best of these indicators require approximately papers to draw conclusion   regarding long term scientific performance with usefully small statistical uncertainties Further the approach described here permits statistical comparison of scientists working in distinct areas of science'
print lemmatize_sentence(senten)

# from nltk.stem.wordnet import WordNetLemmatizer
#
# lem = WordNetLemmatizer()
#
# print lem.lemmatize('people', 'v')

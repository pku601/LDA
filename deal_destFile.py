from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

fp_out = open('destFile_stem.txt', 'wb')
with open('destFile.txt', 'r') as f:
    for line in f:
        tokens = tokenizer.tokenize(line.lower())
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if i not in en_stop]
        # stem token
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        my_list = ' '.join(stemmed_tokens)
        fp_out.write(my_list)
        fp_out.write('\n')
fp_out.close()

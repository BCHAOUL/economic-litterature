import requests
from sys import getsizeof
from bs4 import BeautifulSoup
import numpy as np
import nltk
from nltk import sent_tokenize
from nltk.corpus import stopwords
from gensim.models import word2vec
from sklearn.manifold import TSNE
from sklearn.decompose import PCA
import pandas as pd



from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

def remove_stopwords(text, stopw = stopwords.words("english")):
    list_of_sentences = []
    
    for sentences in text:
        list_of_words = []
        for word in sentences:
            if not word in stopw:
                list_of_words.append(word)
        list_of_sentences.append(list_of_words)
    return list_of_sentences

def clean_sent(sentences):
    """Sentence must be a list containing string"""
    stopw = stopwords.words("english")
    # Lower each word in each sentence        
    sentences = [tokenizer.tokenize(sent.lower()) for sent in sentences]
    sentences = remove_stopwords(sentences)
    return sentences

model = word2vec.Word2Vec(
    min_count = 20,
    size = 300,
    alpha= 0.03
)
model.build_vocab(sents)

model.train(tokens, total_examples= model.corpus_count, epochs = 50)

model.init_sims(replace= True)

all_words = model.wv.syn0

tsne = TSNE(n_components= 3, random_state= 1)

all_words_3dmatrix = tsne.fit_transform(all_words)

points = pd.DataFrame(
    [
        (word, coords[0], coords[1])
        for word, coords in [
            (word, all_words_3dmatrix[model.wv.vocab[word].index])
            for word in model.wv.vocab
        ]
    ],
    columns=["word", "x", "y"]
)


import nltk
from nltk import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import word_tokenize
from nltk.corpus import stopwords
import pandas as pd



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


def word2vec_to_dataframe(model, all_words_matrix):
    points = pd.DataFrame(
        [
            (word, coords[0], coords[1])
            for word, coords in [
                (word, all_words_matrix[model.wv.vocab[word].index])
                for word in model.wv.vocab
            ]
        ],
        columns=["word", "x", "y"])
    return points
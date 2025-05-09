import re
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

def tokenize_text(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word.lower() not in stop_words]

def remove_short_tokens(tokens, min_length=3):
    return [word for word in tokens if len(word) >= min_length]

def clean_html(text):
    return BeautifulSoup(text, "html.parser").get_text()

def preprocess_text(text):
    text = clean_html(text)
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = remove_short_tokens(tokens)
    return tokens

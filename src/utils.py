import nltk
import json
import os
from nltk import word_tokenize, regexp_tokenize, FreqDist
from nltk.stem import WordNetLemmatizer
import string
import re

nltk_data = os.path.join("nltk_data")
nltk.data.path.append(nltk_data)

def text_processing(user_input):
    pattern = "([a-zA-Z]+(?:'[a-z]+)?)"
    review_text = regexp_tokenize(user_input, pattern)
    review_text = ' '.join(review_text)
    review_text = review_text.lower()
    
    stop_path = os.path.join("stopwords.json")
    file = open(stop_path, "r")
    stopwords_list = json.load(file)
    file.close()
    stopwords_list += list(string.punctuation)
    stopwords_list += ['game', 'animal', 'crossing', 'new', 'horizons', 'horizon']
    stopwords_list += list(string.ascii_lowercase)
    review_text = [w for w in review_text.split() if w not in stopwords_list]
    
    lemmatizer = WordNetLemmatizer()
    review_text = [lemmatizer.lemmatize(w) for w in review_text]
    review_text = ' '.join(review_text)
        
    return review_text
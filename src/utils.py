import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, regexp_tokenize, FreqDist
from nltk.stem import WordNetLemmatizer
import string
import re

def text_processing(user_input):
    pattern = "([a-zA-Z]+(?:'[a-z]+)?)"
    review_text = regexp_tokenize(user_input, pattern)
    review_text = ' '.join(review_text)
    review_text = review_text.lower()

    
    stopwords_list = stopwords.words('english')
    stopwords_list += list(string.punctuation)
    stopwords_list += ['game', 'animal', 'crossing']
    review_text = [w for w in review_text.split() if w not in stopwords_list]
    
    lemmatizer = WordNetLemmatizer()
    review_text = [lemmatizer.lemmatize(w) for w in review_text]
    review_text = ' '.join(review_text)
        
    return review_text
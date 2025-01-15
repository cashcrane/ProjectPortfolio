import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))    
    #Tokenize the text
    tokens = nltk.word_tokenize(text)

    # identify industry acronyms
    acronym_pattern = re.compile(r'^[A-Z]{2,}$')

    # Process tokens: skip lemmatization for acronyms and remove stop words
    processed_tokens = [
        token if acronym_pattern.match(token) else lemmatizer.lemmatize(token.lower()) 
        for token in tokens if token.lower() not in stop_words or acronym_pattern.match(token)
    ]
    
    # Re-join the processed tokens into a single string
    processed_text = " ".join(processed_tokens)
    return processed_text

# Define the functions at the top level
def get_activity_text(x):
    return x['ActivityName']

def get_wbs_text(x):
    return x['WBS']

def get_combined_text(x):
    return x['combined']

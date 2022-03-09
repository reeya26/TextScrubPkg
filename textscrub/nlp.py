
#NLP Tasks for Software Design for Data Science
import nltk

#Libraries for Work Tokenization

from nltk.tokenize import word_tokenize

#Libraries for Stop Word Removal
import spacy
#Run the following code below on Terminal
# $python -m spacy download en_core_web_sm
#from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

import spacy

from nltk.stem import WordNetLemmatizer

#Libraries for Working with Emojis
from emoji.core import demojize
import re
import emoji

#Libraries for Emoji
import json
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



"""
    Data Preprocessing Required for NLP Tasks
    Tokenization, Stop Word Removal, Acronym Expansion, Spell Correction, Lemmatization
    Args:
        text(str): raw text
    return args:
"""

def tokenizing(text):

  """
    Splitting the text into tokens
    Args:
        text(str): raw text
    return args[]:

  """

	#Tokenization 

  tokens = word_tokenize(text)

  #print(Levenshtein.distance("Hi","Hie"))
  return tokens


def stopword_removal(text):

  """
    Removing Stop Words (like articles, prepositions, pronouns, conjunctions, etc) 
    that do not add much information to the text.
    Args:
        text(str): raw text
    return args[]:
  """

  #Loading the Small Model of English Stop Words from lib spacy

  en = spacy.load('en_core_web_sm')
  sw_spacy = en.Defaults.stop_words

  #print(sw_spacy)

  words = [word for word in text.split() if word.lower() not in sw_spacy]
  new_text = " ".join(words)


  return new_text



def acronym_expansion(text):

  """
    Converting all acronyms into their full forms
    Args:
        text(str): raw text
    return text:
  """

  en = spacy.load('en_core_web_sm')

  doc = en(text)
  sentences = [sent.text.strip() for sent in doc.sents]
  print(sentences)

def remove_emoji(text, op = "remove"):
  """ 
  Returns the string without the emojis and also the
  string with text translation of the emoji as a tuple
  """

  #Identifying Emojis present in Data
  emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F" # emoticons
                           u"\U0001F300-\U0001F5FF" # symbols & pictographs
                           u"\U0001F680-\U0001F6FF" # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF" # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)

  if(op == "replace"):
   ans = emoji.demojize(text)
   ans = ans.replace(":", "")
   return ans.replace("_", " ")
 
  else:
   return emoji_pattern.sub(r'', text)


def lemmat(text):
  """ 
    Lemmatize individual tokens
    Args:
        text(str): raw text
    return args[]:
  """

  lemmatizer = WordNetLemmatizer()

  tokens = word_tokenize(text)
  new_text = ""

  for t in tokens:
    new_text = new_text + lemmatizer.lemmatize(t) + " "
  

  return new_text


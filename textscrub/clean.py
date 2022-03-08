import unicodedata
import regex as re
import sys

from string import punctuation

import numpy as np
import pandas as pd
import Levenshtein
from sklearn.cluster import dbscan

def remove_glyphs(text):
    """
    Remove all the non-ascii, non-latin and non-printable characters from the raw text
    Args:
        text(str) -- raw text
    Returns:
        text(str) -- text clean from non ascii, non-latin and non-printable characters
    """

    # remove non - ascii characters
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r'[^\x00-\x7F]+','', text)

    # remove accents
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    
    # Get all unicode characters
    all_chars = (chr(i) for i in range(sys.maxunicode))
    # Get all non printable characters
    control_chars = ''.join(c for c in all_chars if unicodedata.category(c) == 'Cc')
    # Create regex of above characters
    control_char_re = re.compile('[%s]' % re.escape(control_chars))
    # remove non-printable characters
    text = control_char_re.sub('', text)

    # remove non-latin characters
    text = re.sub(r'[^\p{Latin}]', '', text)

    return text

def remove_spaces(text):
    """
    Remove all the tabs, spaces, and line breaks from the raw text
    Args:
        text(str) -- raw text
    Returns:
        text(str) -- text clean from tabs, and spaces
    """
    # remove \t, \n, \r
    text = text.replace("\t", "").replace("\r", "").replace("\n","") 
    # remove 2 or more than 2 spaces
    text = re.sub('\s{2,}', " ", text)

    return text

def remove_html_tags(text):
    """
    Remove all html tags from the raw text
    Args:
        text(str) -- raw text
    REturns:
        text(str) -- text clean from html tags
    """

    # create regex for html tags
    html_re = re.compile(r'<.*?>')
    # remove html tags
    text = re.sub(html_re, '', text)

    return text

def remove_hyperlinks(text):
    """
    Remove all hyperlinks and URLs from the raw text
    Args:
        text(str) -- raw text
    Returns:
        text(str) -- text clean from hyperlinks
    """
    text = re.sub(r'https?://\S+', '', text)

    return text

def remove_punctuation(text):
    """
    Remove all punctuations from the raw text
    Args:
        text(str) -- raw text
    Returns:
        text(str) -- text clean from punctuation
    """

    text = re.sub(f"[{re.escape(punctuation)}]", "", text)

    return text

def homog_lev(obj, eps=1, min_samples=2):
    """
    Remove all hyperlinks and URLs from the raw text
    Args:
        dataframe(str) -- almost similar text
    Returns:
        dataframe(str) -- text clean from multiple instances of same value
    """

    def homog_lev_series(obj, eps=eps, min_samples=min_samples):
        name = obj.name

        original = obj.copy()
        obj = obj.drop_duplicates()
        data = obj.tolist()

        def lev_metric(x, y):
            i, j = int(x[0]), int(y[0])
            return Levenshtein.distance(data[i], data[j])

        X = np.arange(len(data)).reshape(-1, 1)
        labels = dbscan(X, metric=lev_metric, eps=eps, min_samples=min_samples)[1]

        x = pd.DataFrame({'A': obj.reset_index(drop=True), 'B': pd.Series(labels)})
        y = x.drop_duplicates('B')
        y = y[~(y.B==-1)]
        y.columns = ['C', 'B']
        x = x.merge(y, on='B', how='left')
        x['C'] = np.where(x.C.isnull(), x.A, x.C)

        results = pd.DataFrame({'A': original})
        results = results.merge(x[['A', 'C']], on='A', how='left')
        out = results.C.rename(name)
        
        return out

    if isinstance(obj, pd.DataFrame):
        for col in obj.columns:
            obj['{}'.format(col)] = homog_lev_series(obj['{}'.format(col)])
    else:
        obj = homog_lev_series(obj)

    return obj
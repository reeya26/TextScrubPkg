import unicodedata
import regex as re
import sys

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
    html_re = re.compile('<.*?>')
    # remove html tags
    text = re.sub(html_re, '', text)

    return text

def remove_hyperlinks(text):
    """
    Remove all hyperlinks and URLs from the raw text
    Args:
        text(str) -- raw text
    Returns:
        text(str) -- text clean from html tags
    """
    text = re.sub(r'https?://\S+', '', text)

    return text


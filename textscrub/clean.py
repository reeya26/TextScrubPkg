import unicodedata
import regex as re
import sys

def remove_non_ascii(text):
    """
    Remove all the non-ascii characters and non-printable characters from the raw text
    Args:
        text(str): raw text
    return args:

    """

    # remove non - ascii characters
    text = text.unicodedata.normalize("NFKD", text)
    text = re.sub(r'[\x00-\x7F]+', '', text)
    
    # Get all unicode characters
    all_chars = (chr(i) for i in range(sys.maxunicode))
    # Get all non printable characters
    control_chars = ''.join(c for c in all_chars if unicodedata.category(c) == 'Cc')
    # Create regex of above characters
    control_char_re = re.compile('[%s]' % re.escape(control_chars))
    # remove non-printable characters
    text = control_char_re.sub('', text)

    return text
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textscrub import clean, nlp

# final function
def normalize_text(
    text,
    remove_glyphs = True,
    remove_html_tags = True,
    remove_hyperlinks = True,
    remove_punctuation = True,
    remove_spaces = True,
    tokenizing = True,
    stopwords_removal = True,
    lemmat = True,
    remove_emojis = True,
    replace_emojis = True
):
    """
    Normalize various aspects of a raw text. A convenience function for applying all other preprocessing functions in one go.
    Args:
        text(str) -- raw text to preprocess
        remove_glyphs(bool) -- it True, remove the non-ascii characters, non-printable characters, non-latin characters, accents.


    Returns:
        str -- prerocessed text.
    """

    if text is None:
        return ""

    text = str(text)

    if remove_glyphs:
        text = clean.remove_glyphs(text)
    if remove_html_tags:
        text = clean.remove_html_tags(text)
    if remove_hyperlinks:
        text = clean.remove_hyperlinks(text)
    if remove_punctuation:
        text = clean.remove_punctuation(text)
    if remove_spaces:
        text = clean.remove_spaces(text)
    if stopwords_removal:
        text = nlp.stopword_removal(text)
    if lemmat(text):
        text = nlp.lemmat(text)
    if remove_emojis:
        text = nlp.remove_emoji(text)
    if replace_emojis:
        text = nlp.remove_emoji(text, "replace" )
    if tokenizing:
        text = nlp.tokenizing(text)

    return text

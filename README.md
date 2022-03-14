# Text-Scrubbing-Package

[![Build Status](https://travis-ci.org/reeya26/TextScrubPkg.svg?branch=master)](https://travis-ci.org/reeya26/TextScrubPkg) 
[![Coverage Status](https://coveralls.io/repos/github/reeya26/TextScrubPkg/badge.svg?branch=master)](https://coveralls.io/github/reeya26/TextScrubPkg?branch=master) 
![Language](https://img.shields.io/badge/language-python-blue.svg)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com//reeya26/TextScrubPkg/blob/master/LICENSE)
![contributors](https://img.shields.io/github/contributors/reeya26/TextScrubPkg.svg) 
![codesize](https://img.shields.io/github/languages/code-size/reeya26/TextScrubPkg.svg) 
![pullrequests](https://img.shields.io/github/issues-pr/reeya26/TextScrubPkg.svg) 
![closedpullrequests](https://img.shields.io/github/issues-pr-closed-raw/reeya26/TextScrubPkg.svg)

<p align="center">
  <img  src="https://github.com/reeya26/TextScrubPkg/blob/main/docs/textimage.png">
</p>

## Introduction
TextScrub is a text-cleaning package which prevents you from spending long hours cleaning web scrapped data, either to prepare for a presentation or for NLP projects. The user can run single line of code to clean the textual data.

## Resources Used
- Editor used: VS code
- Python version: 3.9.4
- Packages used: unicodedata, sys, os, regex, string, numpy, pandas, sklearn, levenshtein, spacy, nltk, emoji

## Project Organization

This package has the following structure.

```
TextScrubPkg/
  |- examples
    |-example.ipynb
  |- textscrub/
    |- __init__.py
    |- clean.py
    |- nlp.py
    |- normalize_text.py
  |- docs/
    |- index.md
    |- textimage.png
  |- tests/
    |- __init__.py
    |- test_clean.py
    |- test_nlp.py
    |- testing_dataset.csv
    |- testing_normalize.py
  |- setup.py
  |- requirements.txt
  |- LICENSE
  |- README.md
```

## Users

- **Analysts**: Requiring quick data-cleaning functionalities, and who are not technically adept
- **Data Scientists**: Programmers wanting to clean web-scrapped data. Focus on experimenting with model-building instead of scrubbing

## Function Description

This package provides two main task specific fucntions:
1. Basic Cleaning for Data Analyis
2. Advanced Cleaning for NLP related tasks

For cleaning the data call the `textscrub.normalize_text.normalize_text(your text)` function. The function parameters defined are as follows:

1. ***remove_glyphs*** - Removes non-ascii characters, non-printable charaters, accents, and non-latin characters
2. ***remove_spaces*** - Remove Extra Spaces, including tabs and line breaks
3. ***remove_html_tags*** - Remove HTML tags
4. ***remove_hyperlinks*** - Remove hyperlinks
5. ***remove_punctuation*** - Remove Puntuation
6. ***tokenizing*** - Tokenization
7. ***stopwords_removal*** - Remove Stopwords
8. ***lemmat*** - Perform Lemmatization
9. ***replace_emojis*** - Replace emojis
10. ***remove_emojis*** - Remove emojis

By default these parameters are true. If you do not require them, then you can set is as *False*.

Apart from this we can normalize a string column as well. To do this, call `textscrub.clean.homogenize_column(col_name)` from the textscrub package.

## How to Use

To test the functionalities of the package, refer to the [Python notebook](https://github.com/reeya26/TextScrubPkg/blob/main/examples/example.ipynb)

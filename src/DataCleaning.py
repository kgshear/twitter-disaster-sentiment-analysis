import string
from nltk.corpus import stopwords
import re

import pandas as pd

def getDataFrame(filepath):
    df = pd.read_csv(filepath)
    return df


def splitFeatures(dataframe, column):
    y_data = dataframe.loc[:, column]
    dropFeature(dataframe, column)
    x_data = dataframe
    return x_data, y_data

def dropFeature(dataframe, column):
    dataframe.drop(column, axis=1, inplace=True)
    return dataframe

def clean_text(text):
    text = remove_tag_and_links(text)
    text = removePunctuation(text)
    text = removeStopwords(text)
    return text

def removePunctuation(text):
    text = text.lower()
    punctuation = string.punctuation + '\n' + '\t'
    for char in punctuation:
        table = str.maketrans(" ", " ", char)
        text = text.translate(table)
    return text

def remove_tag_and_links(text):
    link_tag = re.compile(r'(http\S+)|(www.\S+)|(@\w+)')
    text = re.sub(link_tag, '', text)
    return text

def removeStopwords(text):
    stop = stopwords.words('english')
    stop.remove("not")
    words = text.split()
    clean_text = " ".join([word for word in words if word.lower() not in stop])
    return clean_text


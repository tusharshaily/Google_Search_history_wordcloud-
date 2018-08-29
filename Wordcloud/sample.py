import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from os import path
from wordcloud import WordCloud, STOPWORDS
words = open("words.txt", "w")
data_file='BrowserHistory.json'
with open(data_file) as a:
	data=json.load(a)
for i in range(0,500):
		words.write(data["Browser History"][i]["title"]+ "\n")

text = open('words.txt').read()
stopwords = set(STOPWORDS)

# Generate a word cloud image
wordcloud = WordCloud(width=1200, height=1000,stopwords=stopwords,max_words=100)
wordcloud.generate(text)
wordcloud.to_file("wordcloud.png")

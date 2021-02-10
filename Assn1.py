# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:26:06 2021

@author: Shantanu
"""
#Q1
import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import PunktSentenceTokenizer

movie_reviews.fileids()
movie = movie_reviews.raw('neg/cv614_11320.txt')
custom_sent_tokenizer = PunktSentenceTokenizer(movie)

movie_test = movie_reviews.raw('neg/cv985_5964.txt')
tokenized = custom_sent_tokenizer.tokenize(movie_test)

def process():
    for i in tokenized:
        words = nltk.word_tokenize(i)
        tag = nltk.pos_tag(words)
        print(tag)
        
process()

#Q2
movie_reviews.categories()
movie_reviews.fileids('pos')
pos_rev = movie_reviews.raw('pos/cv991_18645.txt')
cust_pos_token = PunktSentenceTokenizer(pos_rev)
token = cust_pos_token.tokenize(pos_rev)

from nltk.corpus import stopwords
stopword=stopwords.words('english')
print(stopword)

num_text=0
def removestop(num_text):
  for i in tokenized:
    words=nltk.word_tokenize(i)
    if words not in stopword:
      num_text=num_text+1
  print(num_text)
  

removestop(num_text)



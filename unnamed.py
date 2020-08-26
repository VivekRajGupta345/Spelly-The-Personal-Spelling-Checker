# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:20:31 2020

@author: Vivek Raj Gupta
"""

word_database=open("Word_List.txt","r")

words=word_database.readlines()
print(len(words))

#print(word_database.readline())

for word in words:
    print(word.strip(" "))
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:20:31 2020

@author: Vivek Raj Gupta

This script adds all the words in the prefix tree.
It will save the data structure so that search could be faster during run time as no need to initialize the trie.
"""

import time
from trie import Trie

start_time = time.time()
word_database=open("Word_List.txt","r")
words=word_database.readlines()

#print(word_database.readline())

prefix_tree=Trie()

for word in words:
    
    word_mod=word.strip(" ")[:-1]
    
    prefix_tree.add(word_mod)
    

end_time=time.time()

print("Time Taken to execute:"+str(end_time-start_time)+" seconds")

"""
Total words in word database = 370K approx.
Time taken to add all the words to trie database is approximately 35 seconds.

"""
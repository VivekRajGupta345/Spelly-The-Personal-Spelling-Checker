# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:40:07 2020

@author: Vivek Raj Gupta
"""

import pickle
import bz2

import time
start=time.time()
f=bz2.BZ2File("Compressed_Trie.pkl","rb")
end=time.time()

print(end-start)
trie=pickle.load(f)

print(trie.search("ad"))

f.close()


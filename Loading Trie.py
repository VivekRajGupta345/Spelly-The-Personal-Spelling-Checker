# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:40:07 2020

@author: Vivek Raj Gupta
"""

import pickle
import bz2

f=bz2.BZ2File("Compressed_Trie.pkl","rb")

trie=pickle.load(f)

print(trie.search("ad"))

f.close()


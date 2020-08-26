# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:20:51 2020

@author: Vivek Raj Gupta
"""
#single test
from trie import Trie
from string_metric import LevenshteinDistance
prefix_tree=Trie()

prefix_tree.add("awe")
prefix_tree.add("aqwer")
prefix_tree.add("caaaaa")
print(prefix_tree.search("cqaaaa"))

print(LevenshteinDistance("aa","bqaaaa"))


######################################

"""
Looks good on manual testing.
Works as expected.
"""
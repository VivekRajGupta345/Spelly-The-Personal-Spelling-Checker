# Spelly The Personal Spelling Checker
It is a program that accepts a sentence from a user and checks that whether each word is spelled correctly or not, and will give new word suggestions to replace the incorrect spelled word. The user will have an option to accept the suggested word or keep the original word, thus adding it into vocabulary.

# Concepts Used:
1)Trie Data structure  
2)Levenshtein Distance (Populary known as a famous dynamic Programming question- Edit Distance)  
3)Backtracking  

# Libraries used:
1)pickle(for storing the trained Trie data structure)  
2)bz2 (for compression of Trie Data structure)  
3)time  
4) auto-py-to-exe (For converting python program to a desktop app that uses console)  

# Development tools:
1)Spyder4 Ide  
2)Python 3.7 (CPython implementation)  

# Brief Idea
Trie is used to store apprrox 370k words from a word database. This trie is used to search for the word entered by the user using prefix.  
In case a word is not found in database. It will look for the closest words that can match the input word.  
The closeness between two words is determined by their Levenshtein Distance.  

# How to start:
1)Download the code.  
2)Open the Spelly folder.  
3)Double click Spelly.exe  


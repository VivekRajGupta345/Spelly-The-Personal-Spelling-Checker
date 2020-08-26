# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:44:18 2020

@author: Vivek Raj Gupta

Trie is an efficient information reTrieval data structure. Using Trie. 
search complexities can be brought to optimal limit (key length).
Insert and search costs O(key_length)
however the memory requirements of Trie is O(ALPHABET_SIZE * key_length * N) where N is number of keys in Trie. 
There are efficient representation of trie nodes (e.g. compressed trie, ternary search tree, etc.) to minimize memory requirements of trie.
"""

from string_metric import LevenshteinDistance

class trieNode:
    
    def __init__(self):
        
        self._children=[None for i in range(0,26)]
        
        self._isend=False
        
        self._count=0


class Trie:
    
    def __init__(self):
        
        self.__head=trieNode()
        
    def __key(self,letter):
        
        return ord(letter)-ord("a")
    
    def add(self,string):
        
        curr=self.__head
        
        m=len(string)
        
        for i in range(0,m):
            
            key=self.__key(string[i])
            
            if curr._children[key]!=None:
                curr=curr._children[key]
            else:
                
                temp=trieNode()                
                curr._children[key]=temp
                curr=temp
        
        curr._isend=True
        curr._count+=1
    
    def __searchMain(self,curr_node,index,m,key_string,optimal,optimal_dist,optimal_count,curr_string):
        
        if curr_node._isend==True:
                
            candidate_string=curr_string
            edit_dist=LevenshteinDistance(candidate_string,key_string)
            
            if optimal_dist[0]>edit_dist:
                
                optimal_dist[0]=edit_dist
                optimal[0]=candidate_string
                optimal_count[0]=curr_node._count
                
            elif optimal_dist[0]==edit_dist:
                
                if curr_node._count>=optimal_count[0]:
                    optimal_dist[0]=edit_dist
                    optimal[0]=candidate_string
                    optimal_count[0]=curr_node._count
            else:
                return
        
        if index<m:
    
            key=self.__key(key_string[index])
                        
                                    
            if curr_node._children[key]!=None:
                self.__searchMain(curr_node._children[key],index+1,m,key_string,optimal,optimal_dist,optimal_count,curr_string+key_string[index])
                
            else:
                
                count=-1
                for node in curr_node._children:
                    count+=1
                    if node!=None:
                        new_letter=chr(count+ord("a"))
                        self.__searchMain(node,index+1,m,key_string,optimal,optimal_dist,optimal_count,curr_string+new_letter)
                        
            
        else:
            
            count=-1
            for node in curr_node._children:
                count+=1
                if node!=None:
                    new_letter=chr(count+ord("a"))
                    self.__searchMain(node,index+1,m,key_string,optimal,optimal_dist,optimal_count,curr_string+new_letter)

    
    def search(self,key_string):
        
        curr_string=""
        m=len(key_string)
        optimal=[""]
        optimal_dist=[float("inf")]
        optimal_count=[float("-inf")]
        
        self.__searchMain(self.__head,0,m,key_string,optimal,optimal_dist,optimal_count,curr_string)
        
        return optimal[0]
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:44:18 2020

@author: Vivek Raj Gupta
"""
from string_metric import LevenshteinDistance

class trieNode:
    
    def __init__(self):
        
        self.children=[None for i in range(0,26)]
        
        self.isend=False
        
        self.count=0


class Trie:
    
    def __init__(self):
        
        self.head=trieNode()
        
    def __key(self,letter):
        
        return ord(letter)-ord("a")
    
    def add(self,string):
        
        curr=head
        
        m=len(string)
        
        for i in range(0,m):
            
            key=self.__key(string[i])
            
            if curr.children[key]!=None:
                curr=curr.children[key]
            else:
                
                temp=trieNode()                
                curr.children[key]=temp
                curr=temp
        
        curr.isend=True
        curr.count+=1
    
    def __searchMain(self,curr_node,index,m,key_string,flag,optimal,optimal_dist,optimal_count,curr_string):
        if index==m:
            if curr_node.isend==True:
                flag[0]=True
                optimal_dist=0
                optimal_count=curr_node.count
                optimal=curr_string
                return
            else:
                pass
        
        elif flag[0]==True:
            return
        else:
            
            key=self.__key(key_string[index])
            
            if curr_node.isend==True:
                optimal=curr_string+key_string[index]
                optimal_count=curr_node.count
                
                
            if curr_node.children[key]!=None:
                self.__searchMain(curr_node.children[key],index+1,m,key_string,flag,optimal,optimal_dist,optimal_count,curr_string+key_string[index])
                
            else:
                
            
            
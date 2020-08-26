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
        
        curr=self.head
        
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
    
    def __searchMain(self,curr_node,index,m,key_string,optimal,optimal_dist,optimal_count,curr_string):
        
        if curr_node.isend==True:
                
            candidate_string=curr_string
            edit_dist=LevenshteinDistance(candidate_string,key_string)
            
            if optimal_dist[0]>edit_dist:
                
                optimal_dist[0]=edit_dist
                optimal[0]=candidate_string
                optimal_count[0]=curr_node.count
                
            elif optimal_dist[0]==edit_dist:
                if curr_node.count>=optimal_count[0]:
                    optimal_dist[0]=edit_dist
                    optimal[0]=candidate_string
                    optimal_count[0]=curr_node.count
            else:
                return
        
        if index<m:
    
            key=self.__key(key_string[index])
                        
                                    
            if curr_node.children[key]!=None:
                self.__searchMain(curr_node.children[key],index+1,m,key_string,optimal,optimal_dist,optimal_count,curr_string+key_string[index])
                
            else:
                
                count=-1
                for node in curr_node.children:
                    count+=1
                    if node!=None:
                        new_letter=chr(count+ord("a"))
                        self.__searchMain(node,index+1,m,key_string,optimal,optimal_dist,optimal_count,curr_string+new_letter)
                        
            
        else:
            
            count=-1
            for node in curr_node.children:
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
        
        self.__searchMain(self.head,0,m,key_string,optimal,optimal_dist,optimal_count,curr_string)
        
        return optimal[0]
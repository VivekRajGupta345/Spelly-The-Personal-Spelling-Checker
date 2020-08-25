# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:40:25 2020

@author: Vivek Raj Gupta

The Levenshtein distance is a string metric for measuring the difference between two sequences.
 Informally, the Levenshtein distance between two words is the minimum number of single-character edits.
(i.e. insertions, deletions, or substitutions) required to change one word into the other.
Also known as a common Dynamic Programming question Edit Distance.
Tabulation approach is used to solve this problem.
"""

# The goal is to find the minimum operations to convert str1 to str2
def LevenshteinDistance(str1,str2):
    
    m=len(str1)
    n=len(str2)
    
    dp=[]
    
    for i in range(0,m+1):
        temp=[-1 for j in range(0,n+1)]
        dp.append(temp)
    
    #####Initalizing the dp table#####
    for i in range(0,m+1):
        
        for j in range(0,n+1):
            
            if i==0 and j==0:
                dp[i][j]=0
            elif i==0 and j!=0:
                dp[i][j]=j
            elif i!=0 and j==0:
                dp[i][j]=i
    ###################################
    
    for i in range(1,m+1):
        
        for j in range(1,n+1):
            
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                
                delete=1+dp[i-1][j]
                
                replace=1+dp[i-1][j-1]
                
                insert=1+dp[i][j-1]
                
                dp[i][j]=min(delete,replace,insert)
    
    return dp[m][n]
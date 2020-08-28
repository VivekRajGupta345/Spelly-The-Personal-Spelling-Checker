# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:43:14 2020

@author: Vivek Raj Gupta

"""
import pickle
import bz2


class main:
    
    def __init__(self):
        
        f=bz2.BZ2File("Compressed_Trie2.pkl","rb")
        self.__Trie=pickle.load(f)
        f.close()
        del f
    
    def start(self):
        print()
        print()
        print("#######################Spelly The Personal Spelling Corrector###########################")
        print("Created by - Vivek Raj Gupta")
        print()
        request=1
        while(request):
            print("#################################################################################")
            print("Please enter your sentence.")
            
            m=0
            
            while(m==0):
                sentence=input().strip(" ").split(" ")
                m=len(sentence)
                full_stop=False
                for i in range(0,m):
                    break_flag=False
                    n=len(sentence[i])
                    for j in range(0,n):

                        if i!=m-1:
                            if sentence[i][j].isalpha():
                                pass
                            else:
                                print("Please only use alphabets.")
                                break_flag=True
                                break
                        else:
                            if sentence[i][-1]==".":
                                if len(sentence[i])==1:
                                    print("Please enter a valid sentence.")
                                    break_flag=True
                                    break
                                else:
                                    full_stop=True
                            else:
                                if sentence[i][j].isalpha():
                                    pass
                                else:
                                    print("Please only use alphabets.")
                                    break_flag=True
                                    break
                
                    if break_flag==True:
                        m=0
                        break
                if m==1 and sentence[0]=="":
                    print("Please enter a valid sentence.")
                    m=0
                    
            if full_stop==True:
                sentence[-1]=sentence[-1][:-1]
                
            suggested_sentence=[]
            
            for word in sentence:
                
                temp_word=word.lower()
                
                suggested_word=self.__Trie.search(temp_word)
                
                if word[0].isupper():
                    suggested_word=suggested_word[0].upper()+suggested_word[1:]
                    
                suggested_sentence.append(suggested_word)
                
            output_sentence=[]
            
            
            for i in range(0,m):
                
                if sentence[i]!=suggested_sentence[i]:
                    print()
                    print("Spelling Error Detected :",end=" ")
                    print(sentence[i])
                    
                    print("Suggested Word :",end= " ")
                    print(suggested_sentence[i])
                    
                    print("Press 1 to accept the change or press 0 to to use the origional word.")
                                    
                    flag=0
                    while(flag==0):
                        
                        inp=input()
                        try:
                            inp=int(inp)
                            
                            if inp!=1 and inp!=0:
                                print("Please enter a valid input.")
                                print("Press 1 to accept the change or press 0 to to use the origional word.")
                            else:
                                flag=1
                                
                        
                        except:
                            print("Please enter a valid input.")
                            print("Press 1 to accept the change or press 0 to to use the origional word.")
                             
                             
                    if inp==1:
                        output_sentence.append(suggested_sentence[i])
                        self.__Trie.add(suggested_sentence[i].lower())
                    else:
                        output_sentence.append(sentence[i])
                        self.__Trie.add(sentence[i].lower())
                
                else:
                    output_sentence.append(sentence[i])
                    self.__Trie.add(sentence[i].lower())
                    
                    
                    
                    
            final_sentence=""
            
            for word in output_sentence[:-1]:
                final_sentence+=word+" "
                
            final_sentence+=output_sentence[-1]
            
            if full_stop==True:
                final_sentence+="."
                
            print("Revised Sentence :")
            print(final_sentence)
            
            print("#################################################################################")
            print()
            
            print("Enter 1 to write a sentence or press 0 to exit the application.")
            
            flag=0
            while(flag==0):
                
                inp=input()
                try:
                    inp=int(inp)
                    
                    if inp!=1 and inp!=0:
                        print("Please enter a valid input.")
                        print("Enter 1 to write a sentence or press 0 to exit the application.")
                    else:
                        flag=1
                        
                        if inp==1:
                            break
                        else:
                            request=0
                            sfile=bz2.BZ2File("Compressed_Trie.pkl","wb")
                            pickle.dump(self.__Trie,sfile,-1)
                            sfile.close()
                            break
                except:
                    print("Please enter a valid input.")
                    print("Enter 1 to write a sentence or press 0 to exit the application.")
        
            
        
        
main=main()

main.start()
                
        
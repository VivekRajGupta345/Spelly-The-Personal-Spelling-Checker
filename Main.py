# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:43:14 2020

@author: Vivek Raj Gupta

"""
import pickle
import bz2


class main:
    
    def __init__(self):
        
        f=bz2.BZ2File("Compressed_Trie.pkl","rb")
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
            
            sentence=input().strip(" ").split(" ")
            m=len(sentence)
            
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
                        self.__Trie.add(suggested_sentence[i])
                    else:
                        output_sentence.append(sentence[i])
                        self.__Trie.add(sentence[i])
                
                else:
                    output_sentence.append(sentence[i])
                    self.__Trie.add(sentence[i])
                    
                    
                    
                    
            final_sentence=""
            
            for word in output_sentence:
                final_sentence+=word+" "
            
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
                
        
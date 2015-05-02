'''
@author: Kyle Vonderwerth, StuID: 50183290
Created on Apr 10, 2015
INF 141: Information Retrieval 
Assignment 1
https://github.com/Morphaz
WordFrequencyCounter.py
Python 34

'''
import Utilities
from collections import defaultdict
from Frequency import Frequency

def wordFrequencyCount(tokens : [str]) -> [Frequency]:
     '''
     Counts frequency of words from a tokenized list. 
     '''
     if not tokens: #check if list is empty, [] == False
          return []      
     
     tempFreq = defaultdict(int) #accumulator for frequency count
     
     for token in tokens:
          '''
          iterate of tokens, using a defaultdict(int) with the 2gram as key and count duplicates for value
          '''
          if token != '': #only make a modification to the dictionary if the token is not an empty string
               tempFreq[token] += 1 
     
     return tempFreq
     
#if __name__ == '__main__':
     #Utilities.writeFrequencies(wordFrequencyCount(Utilities.tokenizeFile(open('.txt').read())))
               
           
          
          
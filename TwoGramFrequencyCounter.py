'''
@author: Kyle Vonderwerth, StuID: 50183290
Created on Apr 10, 2015
INF 141: Information Retrieval 
Assignment 1
https://github.com/Morphaz
TwoGramFrequencyCounter.py
Python 34

'''
import Utilities
from Frequency import Frequency
from collections import defaultdict

def twoGramFrequencyCount(tokens : [str]) -> [Frequency]:
     '''
     Counts frequency of 2grams from a tokenized list. 
     '''
     if not tokens: #check if list is empty, [] == False
          return []
     
     tokens = list(filter(lambda x: x !='', tokens))    #filters out empty strings
     
     tempFreq = defaultdict(int)
     
     for twoGram in zip(tokens,tokens[1:]): # for (token,token) in [(token,token)]
          '''
          iterate over a list of the combined list of words and the off-set list of words to create the twoGrams,
          using a defaultdict(int) with the 2gram as key and count duplicates for value
          '''
          tempFreq[' '.join(list(twoGram))] += 1 # tempFreq['token token'] = frequency value
     
     return Utilities.collateFrequencies(tempFreq)

if __name__ == '__main__':
     Utilities.printFrequencies(twoGramFrequencyCount(Utilities.tokenizeFile(open('xyz.txt').read())))
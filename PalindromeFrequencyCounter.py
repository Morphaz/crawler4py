'''
@author: Kyle Vonderwerth, StuID: 50183290
Created on Apr 10, 2015
INF 141: Information Retrieval 
Assignment 1
https://github.com/Morphaz
palindromeFrequencyCounter.py
Python 34

'''
import Utilities
from Frequency import Frequency
from collections import defaultdict


def palindromeFrequencyCount(tokens : [str]) -> [Frequency]:
     '''
     Counts the frequency of palindromes in a given list of tokens
     '''
     if not tokens: #check if list is empty, [] == False
          return []
     
     tempFreq = defaultdict(int) 
     palindromeAccumulator = '' '' #The variable accumulates tokens into a string until a palindrome is form  
     tokens.append('addOne') #For the algorithm to work it is necessary that the last token ends a palindrome
    
     for i in range(len(tokens)): 
          '''
          iterates for the length of the tokens list. Each iteration checks palindromAccumulator and the reverse of palindrome accumulator twice.
          if checks for non-matches and catches the empty string(entry case). When true, appends token[i] to palindromeAccumulator
          else there is a palindrome. tempFreq is incremented and palindromeAccumulator is reset to token[i]
          '''
          if palindromeAccumulator != palindromeAccumulator[::-1] or palindromeAccumulator == '': # compare pal and revesed pal; check for pal
               palindromeAccumulator += tokens[i] #concatenate tokens[i] to palindromeAccumulator
          else:
               tempFreq[palindromeAccumulator] += 1 # assign value to dict 
               palindromeAccumulator = tokens[i] #reset to palindromeAccumulator to tokens[i]
     
     return Utilities.collateFrequencies(tempFreq) 

if __name__ == '__main__':
     Utilities.printFrequencies(palindromeFrequencyCount(Utilities.tokenizeFile(open('test.txt').read())))
               
               
               
               
     
     
     
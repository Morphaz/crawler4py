'''
@author: Kyle Vonderwerth, StuID: 50183290
Created on Apr 10, 2015
INF 141: Information Retrieval 
Assignment 1
https://github.com/Morphaz
Utilities.py
Python 34
''' 
from Frequency import Frequency
from collections import defaultdict

ALPHANUMERICS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

def tokenizeFile(tokens: [str]) -> [str]:
     '''
     This function takes a string argument and uses a map/filter transform on it, returning a alphanumeric, all lower case tokenized list. 
     '''
     #for token in str(open("stopWords.txt","r").read()).strip("\n"):
          #tokens = tokens.replace(token,"")
          #print(token)
     def alphaNumericFilter(token : str) -> str:
          '''
          This function utilizes lambda to check if a char in a token is alphanumeric, filtering the token and returning a token that is 
          only alphanumeric and normalized to lowercase.
          '''
          return ''.join(filter(lambda x: x in ALPHANUMERICS, token)).lower() 
     
     return list(map(alphaNumericFilter,tokens.split())) 

def collateFrequencies(tempFreq : defaultdict()) -> [Frequency]:
     '''
     instantiates Frequencies from a defaultdict's key,value pair,
     then sorts the list first by most frequent and second, alphabetically 
     '''
     frequencies = [] 
     
     for key, value in tempFreq.items():
          '''
          iterate over the defaultdict extracting each entry's key,value pair as arguments for instantiated Frequencies 
          ''' 
          frequencies.append(Frequency(key,value)) 
     
     def freqSort(x):
          '''
          sorts by greatest frequency and then alphabetically
          '''
          return (-x.getFrequency(), x.getText()) 
          
     return sorted(frequencies, key = freqSort) 
     
def writeFrequencies(frequencies: []) -> print():
     '''
	Takes a list of word or 2-gram frequencies and prints the total words and unique words in the list and then the formatted contents
	of the frequency list
	'''
     total = 0 # for total count
     
     for frequency in frequencies:
          '''
          iterates over frequencies, accumulating the total by adding up all Frequency.getFrequency()
          '''
          total += int(frequency.getFrequency())
          
     if ' ' in frequencies[0].getText(): # Check if the frequency list contains 2-grams by checking for a space between words
          print('Total 2-gram count: ' + str(total))
          print('Unique 2-gram count: ' + str(len(frequencies)) + '\n') #len(frequencies) = total unique tokens
     else:
          print('Total item count: ' + str(total))
          print('Unique item count: ' + str(len(frequencies)) + '\n')
              
     for frequency in frequencies:
          '''
          iterates over frequencies, printing each Frequency nicely formatted  
          '''
          with open('CommonWords.txt','a') as f:
               f.write('{0:<20} {1}\n'.format(str(frequency.getText()),str(frequency.getFrequency()))) 



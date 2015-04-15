'''
@author: Kyle Vonderwerth, StuID: 50183290
Created on Apr 10, 2015
INF 141: Information Retrieval 
Assignment 1
https://github.com/Morphaz
Frequency.py
Python 34
'''
class Frequency:
     def __init__(self, word : str, frequency = 0):
          '''
          Rather then use multiple constructors the same effect in the java version of this class can be replicated in Python by 
          simply giving a default value to the frequency argument.
          When Frequency class is constructed, if a value for self.frequency is not passed it will be given the default value of 0
          ''' 
          self.word = word
          self.frequency = frequency
     
     def getText(self) -> str:
          return self.word
     
     def getFrequency(self) -> int:
          return self.frequency
     
     def incrementFrequency(self):
          self.frequency += 1
          
     def __str__(self):
          '''
          I have emulated the result of overriding toString with the value in the Java version by overriding the classes built-in
          .str() method. It works like this:  print(Frequency) for a string representing the Frequency values printed to screen. 
          '''
          return self.word + ":" + str(self.frequency)
    
    
    
    
    
    
    
        
    
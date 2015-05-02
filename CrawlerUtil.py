'''
Created on Apr 10, 2015
INF 141: Information Retrieval 
Assignment 2
https://github.com/Morphaz
CrawlerUtil.py
Python 34
'''
import os,Utilities
from os import listdir,stat
from WordFrequencyCounter import wordFrequencyCount
from bs4 import BeautifulSoup
from collections import defaultdict  , OrderedDict
from test.support import sortdict

def crawlerWordFrequencies():
     '''For each file in directory gather all text from text meaningful tags, tokenize that, then add it to a WordFrequencyCounter;
     repeat for each file.''' 
     def freqSort(x):
          '''
          sorts by greatest frequency and then alphabetically
          '''
          return (-x[1], x[0])
     
     parsedCount = 1
     wordFreqs = dict()
     for fileName in os.listdir("data/content"):
          if os.stat("data/content/"+fileName)[6] > 0:
               try:
                    with open("data/content/"+fileName) as mUp:
                         wordFreqs.update(wordFrequencyCount(Utilities.tokenizeFile(BeautifulSoup(mUp.read()).get_text())))
               except:
                    continue
               finally:
                    parsedCount+=1  
     
     tupForm = [(k,v) for k,v in wordFreqs.items()]
     topFH = 0
     for item in sorted(tupForm,key = lambda x: freqSort(x)): 
          if topFH == 500:
               break
          with open('CommonWords.txt','a') as f:
               f.write('{0:<20} {1}\n'.format(str(item[0]),str(item[1])))
          topFH +=1
          
     print('Completed Word Frequency Accumulation')
crawlerWordFrequencies()

def serverStats():
     '''for each line in file accumulate subdomain into diction, then write to file.'''
     def freqSort(x):
          return (-x[1], x[0])
     
     serverDict = defaultdict(int)
     with open("data/webinfo/log.txt") as domains:
          try:
               for line in domains.readlines():
                    serverDict[line.split()[1].split('.edu')[0] +'.edu'] += 1
          finally:
               domains.close()
     
     tupForm = [(k,v) for k,v in serverDict.items()]
     for item in sorted(tupForm,key = lambda x: freqSort(x)): 
          with open('Subdomains.txt','a') as f:
               f.write(str(item[0])+" "+str(item[1])+"\n")
     print("Completed Sub-domain Frequency Accumulation")
serverStats()
     





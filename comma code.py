# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 00:01:05 2020

@author: Umang Gulati
"""

l= ['a', 'b', 'c' , 'd' , 'e', 'f']
def comma(spam):
      str1= ' '
      for i in range(len(spam)-1):
             str1  =str1 + str(spam[i] + ', ')
      
      str1=str1 + str('and' +' ' + spam[len(spam)-1])
      return(str1)
      
print(comma(l))
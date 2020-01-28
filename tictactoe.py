# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 04:43:33 2020

@author: Umang Gulati
"""

theboard={'top-l':' ', 'top-m': ' ', 'top-r':' ',
          'mid-l': ' ','mid-m':' ', 'mid-r': ' ',
          'low-l': ' ','low-m':' ', 'low-r': ' '}
def printboard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
    print('-+-+-')
    
printboard(theboard)

turn= 'X'
for i in range(9):
    printboard(theboard)
    print('Turn for'+ turn + 'Moveonwhich space?')
    move = input()
    theboard[move]= turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
printboard(theboard)
    
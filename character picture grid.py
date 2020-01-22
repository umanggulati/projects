# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:06:15 2020

@author: Umang Gulati
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]





for i in range(len(grid[0])):
    print()
    for j in range(len(grid)):
         print(grid[j][i], end='')
         
    
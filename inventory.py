# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 01:14:54 2020

@author: Umang Gulati
"""
allinventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayinventory(inventory):
    numinventory=0
    for k , v in inventory.items():
        print(str(v) + ' ' + k)
        numinventory = numinventory + v
    print(str(numinventory))
displayinventory(allinventory)
    
    
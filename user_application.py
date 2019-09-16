import pandas as pd
import numpy as np
from datetime import date


# algoirthum trading
# apple - import data source
# Assign `Adj Close` to `daily_close`
daily_close = aapl[['___________']]

# Daily returns
daily_pct_change = daily_close.__________()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)

# Print daily log returns
print(daily_log_returns)
# Resample `aapl` to business months, take last observation as value 
monthly = aapl._________('BM').apply(lambda x: x[-1])


# Resample `aapl` to quarters, take the mean as value per quarter
quarter = aapl.resample("4M").mean()

# Calculate the quarterly percentage change
quarter.__________()

# Daily returns
daily_pct_change = ___________ / daily_close.shift(1) - 1

# Print `daily_pct_change`
print(___________)
# In [1]:
import configparser  # 1 
import oandapy as opy  # 2

config = configparser.ConfigParser()  # 3
config.read('oanda.cfg')  # 4

oanda = opy.API(environment='practice',
                access_token=config['oanda']['access_token'])  # 5
# -*- coding: utf-8 -*-
'''
An auto-balanced binary tree!
'''
import math
import random
class my_queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0
    def isEmpty(self):
        return self.head == self.tail
    def push(self,data):
        self.data.append(data)
        self.tail = self.tail + 1
    def pop(self):
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret
    def count(self):
        return self.tail - self.head
    def print(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])
        
class my_node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    def getdata(self):
        return self.data
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def getheight(self):
        return self.height
    def setdata(self,data):
        self.data = data
        return
    def setleft(self,node):
        self.left = node
        return
    def setright(self,node):
        self.right = node
        return
    def setheight(self,height):
        self.height = height
        return

def getheight(node):
    if node is None:
        return 0
    return node.getheight()

def my_max(a,b):
    if a > b:
        return a
    return b
    def leftrotation(node):
        r'''
            A                      B
           / \                    / \
          B   C                  Bl  A
         / \       -->          /   / \
        Bl  Br                 UB Br  C
       /
     UB
  
    UB = unbalanced node  
    '''
    print("left rotation node:",node.getdata())
    ret = node.getleft()
    node.setleft(ret.getright())
    ret.setright(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret

def rightrotation(node):
    '''
        a mirror symmetry rotation of the leftrotation
    '''
    print("right rotation node:",node.getdata())
    ret = node.getright()
    node.setright(ret.getleft())
    ret.setleft(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret
def rlrotation(node):
    r'''
            A              A                    Br      
           / \            / \                  /  \
          B   C    RR    Br  C       LR       B    A
         / \       -->  /  \         -->    /     / \
        Bl  Br         B   UB              Bl    UB  C  
             \        /
             UB     Bl
    RR = rightrotation   LR = leftrotation
    '''
    node.setleft(rightrotation(node.getleft()))
    return leftrotation(node)

def lrrotation(node):
    node.setright(leftrotation(node.getright()))
    return rightrotation(node)


def insert_node(node,data):
    if node is None:
        return my_node(data)
    if data < node.getdata():
        node.setleft(insert_node(node.getleft(),data))
        if getheight(node.getleft()) - getheight(node.getright()) == 2: #an unbalance detected
            if data < node.getleft().getdata():       #new node is the left child of the left child
                node = leftrotation(node)
            else:
                node = rlrotation(node)             #new node is the right child of the left child
    else:
        node.setright(insert_node(node.getright(),data))
        if getheight(node.getright()) - getheight(node.getleft()) == 2:
            if data < node.getright().getdata():
                node = lrrotation(node)
            else:
                node = rightrotation(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    return node
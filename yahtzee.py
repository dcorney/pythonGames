#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 09:00:13 2015

Yahtzee-kinda game (for me to learn more Python)

@author: dcorney
"""

import random

random.random()

nDice=5

def countNs(diceValues, n):
    score=0
    for x in diceValues:
        if(x==n):
            score+=1
    return score

#Figure out how to generalise (via partial?) these functions
def countOnes(values):
    return 1 * countNs(values,1)
    
def countTwos(values):
    return 2 * countNs(values,2)
    
def countThrees(values):
    return 3 * countNs(values,3)
            
def countFours(values):
    return 4 * countNs(values,4)
            
def countFives(values):
    return 5 * countNs(values,5)
        
def countSixes(values):
    return 6 * countNs(values,6)
    
def nOfAKind(values,n):
    for r in range (1,7):
        if countNs(values,r) >= n:
            return True
    return False

def pair(values):
    if nOfAKind(values,2) == True:
        return 5
    else:
        return 0

def triple(values):
    if nOfAKind(values,3) == True:
        return 17
    else:
        return 0

def quadruple(values):
    if nOfAKind(values,4) == True:
        return 24
    else:
        return 0
        
        
def yahtzee(values):
    if nOfAKind(values,nDice) == True:
        return 50
    else:
        return 0

def fullHouse(values):
    freqsMap = {}
    for v in values:
        freqsMap[v] = freqsMap.get(v, 0) + 1
    freqs = freqsMap.values();
    freqs.sort(reverse = True)
    if len(freqs) <2:
        return 0
    if freqs[0]>=3 and freqs[1] >=2:
        return 25
    return 0
    
def straightLength(values):
    uniques=list(set(values))
    uniques.sort()
    longest=0
    thisSeq=0
    for i in range(1,len(uniques)):
        #print ("i=%d  u[i]=%d u[i-1]=%d" % (i,uniques[i],uniques[i-1]))
        if uniques[i]== 1+uniques[i-1]:
            thisSeq=thisSeq+1
        else:
            longest=thisSeq
            thisSeq=0
    return max(longest,thisSeq)+1

def smallStraight(values):
    if straightLength(values)>=4:
        return 30
    else:
        return 0
        
def largeStraight(values):
    if straightLength(values)>=5:
        return 40
    else:
        return 0
    
def chance(values):
    return sum(values)
    
""" Dice handling """
def rollOneDice():
    return random.randint(1,6)
    
def showDice(values):
    print ("Your dice ")    
    for i in range (1,1+len(values)):
        print ("%c\t" % (64+i)),
    print
    for d in values:
        print ("%d\t"% d),  #trailing ',' means no newline    
    print
        
def pickDice():    
    values=[]
    for x in range(0, nDice):
        values = values + [random.randint(1,6)]
    showDice(values)
    for reroll in range (0,2):
        
        toRoll = raw_input ("Choose dice to re-roll")
        print (toRoll)
        for r in toRoll:
            index = ord(r)-65
            print ("%c  %d" % (r , index))
            if index >=0 and index < nDice:
                values[index]=random.randint(1,6)
        showDice(values)
    return values
    
handTypes = [{"name" : "Count the ones",   "valid":True, "score":0, "fn":countOnes, "pos":1},
             {"name" : "Count the twos",   "valid":True, "score":0, "fn":countTwos, "pos":2},
             {"name" : "Count the threes", "valid":True, "score":0, "fn":countThrees,"pos":3},
             {"name" : "Count the fours", "valid":True, "score":0, "fn":countFours,"pos":4},
             {"name" : "Count the fives", "valid":True, "score":0, "fn":countFives,"pos":5},
             {"name" : "Count the sixes", "valid":True, "score":0, "fn":countSixes,"pos":6},
             {"name" : "Pair", "valid":True, "score":0, "fn":pair,"pos":7},
             {"name" : "Three of a kind", "valid":True, "score":0, "fn":triple,"pos":8},
             {"name" : "Four of a kind" , "valid":True, "score":0, "fn":quadruple,"pos":9},
             {"name" : "Full House" , "valid":True, "score":0, "fn":fullHouse,"pos":10},
             {"name" : "Small Straight" , "valid":True, "score":0, "fn":smallStraight,"pos":11},
             {"name" : "Large Straight" , "valid":True, "score":0, "fn":largeStraight,"pos":12},
             {"name" : "Yahtzee!" , "valid":True, "score":0, "fn":yahtzee,"pos":13},
             {"name" : "Chance" , "valid":True, "score":0, "fn":chance,"pos":14}]


             

"""game starts here!"""
total=0
for round in range(0,len(handTypes)):
        
    #showDice (D)
    D = pickDice()
    
    print ("Your options: ")
    validPos=[]
    for o in handTypes:
        if o['valid'] == True:
            print (o['pos'], o['name'],o['fn'](D))
            validPos.append(o['pos'])
    
    print ('Choose from ', validPos)
    choice = input()
    print ('You chose ', choice)
    """ Check if choice is in validPos"""
    if (choice in validPos):
        for o in handTypes:
            if o['pos']==choice:
                o['valid']=False
                total+=o['fn'](D)
    
    print ('Current score: %d' % total)
        
        
print ('FINAL SCORE: %d' % total)

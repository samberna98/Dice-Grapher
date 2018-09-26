#  File: Dice.py
#  Description: Program that simulates two dice rolls and tabulates the combined results on a graph
#  Date Created: 9/10/17
#  Date Last Modified: 9/11/17

import random

def round(x, t):
    x *= (100/ t)
    if x % 1 >= .5:
        x = int(x+1)
    else:
        x = int(x // 1)
    return x
    
def main():
    random.seed(1234)
    trials = int(input("How many times do you want to roll the dice? ")) # prompt user for number of trials, convert input to int
    cntr = 0 # counter for while loop 
    results = [0,0,0,0,0,0,0,0,0,0,0]
   
    while cntr < trials:
        f = random.randint(1,6) # first dice
        s = random.randint(1,6) # second dice
        tot = f + s # total dice score
        i = 0 # counter for iterating through results list
        while i < len(results): # while loop that fills results list
            if i == tot - 2:
                 results[i] += 1
            i += 1
        cntr += 1
        
    print("Results: " + str(results)) # display results
    print("")
    listMax = 0
    x = 0

    if trials > 100:
        t = 0
        while t < len(results):
            results[t] = round(results[t], trials)
            t += 1
    # print("results: " + str(results)) # debug print
    
    while x < len(results): # while loop to establish max in results list
        if listMax < results[x]:
            listMax = results[x]
        x += 1
        
    # print("listMax = ",listMax)   # debug print
    z = 0
    while z < listMax: # displaying graph
        outp = "|  "
        y = 0
        while y < len(results):
            if results[y] >= listMax:
                outp += "*  "
            else: 
                outp += "   "
            y += 1
        print(outp)
        listMax -= 1
           
    print("+--+--+--+--+--+--+--+--+--+--+--+-")
    print("   2  3  4  5  6  7  8  9 10 11 12")
   
main()
        
        

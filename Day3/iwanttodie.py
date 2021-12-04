# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 23:51:15 2021

@author: Chyt
"""

from collections import Counter

#with open(r"C:\\Users\Chyt\Documents\GitHub\advent-of-code-2021\Day3\exmp.txt") as f:
    #lines = f.readlines()

a_file = open(r"C:\\Users\Chyt\Documents\GitHub\advent-of-code-2021\Day3\input.txt")
file_contents = a_file.read()
lines = file_contents.splitlines()

def pt1(inp):
    gam = []
    eps = []
    tst = []
    
    for n, item in enumerate(inp):
        for l in inp:
            if(n < len(l)):
                tst.append(l[n])
                #print(tst)
            else:
                break
        if(tst == []):
            break
        else:
            count = Counter(tst)
            gam.append(count.most_common(1)[0][0])
            eps.append(count.most_common()[-1][0])
            tst = []
            n+= 1
        
    
    g_string = "".join(gam)
    g = int(g_string, 2)
    
    e_string = "".join(eps)
    e = int(e_string, 2)
    
    power =  e * g
    
    print(power)
    
def oxy(inp):
    oxcalc = []
    n = 0

    for item in enumerate(inp):
        tst = []
        #print("n is:", n)
        #print(inp)
        for l in inp:
            tst.append(l[n])
        
        #print(tst)
        count = Counter(tst)
        #print(count)
        x = list(count.values())
        if(x[0] == x[1]):
            common = "1"
        else:
            common = count.most_common(1)[0][0]
    
        for l in inp:
            if(l[n] == common):
                oxcalc.append(l)
    
        #print(oxcalc)
        
        if(len(oxcalc) > 1):
            n += 1
            inp = oxcalc
            oxcalc = []
        else:
            print(oxcalc)
            return oxcalc
            break

def co2(inp):
    co2calc = []
    n = 0

    for item in enumerate(inp):
        tst = []
        #print("n is:", n)
        #print(inp)
        for l in inp:
            tst.append(l[n])
        
        #print(tst)
        count = Counter(tst)
        x = list(count.values())
        if(x[0] == x[1]):
            common = "0"
        else:
        #print(count)
            common = count.most_common()[-1][0]
    
        for l in inp:
            if(l[n] == common):
                co2calc.append(l)
    
        #print(co2calc)
        
        if(len(co2calc) > 1):
            n += 1
            inp = co2calc
            co2calc = []
        else:
            print(co2calc)
            return co2calc
            break
        
def pt2():
     carbon = co2(lines)
     oxygen = oxy(lines)
     
     c_string = "".join(carbon)
     c = int(c_string, 2)
     o_string = "".join(oxygen)
     o = int(o_string, 2)
     
     support = o * c
     print(support)
        
pt2()     
pt1(lines)
        
        
        
    
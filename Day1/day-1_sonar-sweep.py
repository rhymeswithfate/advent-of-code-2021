# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:49:27 2021

@author: Chyt
"""
import numpy as np

filename = np.genfromtxt(
    r"C:\Users\Chyt\Documents\GitHub\advent-of-code-2021\Day1\puzzle1.txt",
    dtype=int,
    delimiter="\n")

def larger_measurement(sonar_report):
    count = 0
    for i in range(len(sonar_report) - 1):
        j = sonar_report[i]
        k = sonar_report[i + 1]
        if k > j:
            count = count + 1
            
    print(count)
    
def sliding_window(sonar_report):
    count = 0
    for i in range(len(sonar_report) - 3):
        j = sonar_report[i] + sonar_report[i + 1] + sonar_report[i + 2]
        k = sonar_report[i + 1] + sonar_report[i + 2] + sonar_report[i + 3]
        if k > j:
            count = count + 1
            
    print(count)

larger_measurement(filename)
sliding_window(filename)

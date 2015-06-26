#!/usr/bin/python -tt

import random
import io
import sys
import time

def main():
  # Open the file with the problems to read
  try:
    f = open('problems.txt', 'rU')
  except IOError:
    sys.stderr.write('problem occured!!! sc')

  res = []
  prob_sol = () 
  prob_solutes = []

  for line in f:
    res = line.split()
    prob_sol = (res[0], res[1], res[2])
    prob_solutes.append(prob_sol)
  
  rand = random.randint(0,100)

  equal = input("problem: " + str(prob_solutes[rand]))
  
  
  

  f.close()

if __name__ == '__main__':
  main()

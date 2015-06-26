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
  live = 0
  escape = False

  while not escape and live < 3:
    equal = input("problem: " + str(prob_solutes[rand][0]) + " + " \
      + str(prob_solutes[rand][1] + " = "))
    print 'your ans   ', equal
    print 'your lives:', live
    if equal == int(prob_solutes[rand][2]):
      escape = True
    live += 1
  
  if live == 3:
    print 'sorry the corrent answer was', prob_solutes[rand][2]
  else:
    print 'good job on the correct answer!! (answer: )', prob_solutes[rand][2]
  

  f.close()
  sys.exit(0)

if __name__ == '__main__':
  main()

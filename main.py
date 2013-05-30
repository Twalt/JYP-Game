#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 Arjun <Arjun@HYPERION>
#  
from character import Character
from weapon import weapon
from item import Location
import random
import armor
import sys

def main():
	try:
		valid = True
		you = Character(Location(25,35))
	
		while valid:
			var = input("What would you like to do? : ")
			if var == 'quit':
				valid = False
			var = inputValidation(var)
		
		
		xVal = random.randint(1, 49)
		yVal = random.randint(1, 22)
	except KeyboardInterrupt:
		print("\nQuitting")
		
def inputValidation(var):
	outVal = 0
	if var[:4] == 'move' or var[:4] == 'walk':
		if var[5:12] == 'forward':
			outVal = 1
	if var[:4] == 'turn':
		print(var[5:9])
		if var[5:8] == 'left':
			outVal = 2
		if var[5:9] == 'right':
			outVal = 3
			
	return outVal
	
main()


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
		#prints location of you - loc is Location val
		print(you.loc)
		while valid:
			var = input("What would you like to do? : ")
			if var == 'quit':
				valid = False
			#checks input for a command
			var = inputValidation(var)
			if var == -1:
				print("I do not understand that command")
			elif var == 1:
				print(you.loc)
		
		
		xVal = random.randint(1, 49)
		yVal = random.randint(1, 22)
	except KeyboardInterrupt:
		print("\nQuitting")
		
def inputValidation(var):
	outVal = -1
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


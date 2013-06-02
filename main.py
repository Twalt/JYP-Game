#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 Arjun <Arjun@HYPERION>
#  
from character import Character
from character import Compass
from weapon import weapon
from item import Location
import random
import armor
import sys

def main():
	try:
		valid = True
		you = Character(Location(25,35), Compass(0))
		#prints location of you - loc is Location val
		generateItems()
		
		while valid:
			print(you.loc)
			var = input("What would you like to do? : ")
			command = var.split(' ')
			if command[0] == 'quit':
				valid = False
				
			#checks input for a command
			inVal = inputValidation(command)
			if inVal == -1:
				print("I do not understand that command")
			elif inVal == 1:
				howMuch = moveDist(command)
				if howMuch == 0:
					print("Invalid move distance")
				moveYou(you, howMuch)
			elif inVal == 2:
				you.compass.direction -= 1
				if you.compass.direction < 0:
					you.compass.direction += 4
			elif inVal == 3:
				you.compass.direction += 1
				if you.compass.direction > 3:
					you.compass.direction -= 4
			elif inVal == 4:
				you.compass.direction += 2
				if you.compass.direction > 3:
					you.compass.direction -= 4
			elif inVal == 5:
				print(you.compass)
	except KeyboardInterrupt:
		print("\nQuitting")

def generateItems():	
	xVal = random.randint(1, 49)
	yVal = random.randint(1, 22)

def moveYou(you, x):
	#North
	if you.compass.direction == 0:
		you.loc = Location(you.loc.x, you.loc.y - x)
	#East
	elif you.compass.direction == 1:
		you.loc = Location(you.loc.x + x, you.loc.y)
	#South
	elif you.compass.direction == 2:
		you.loc = Location(you.loc.x, you.loc.y + x)
	#West
	elif you.compass.direction == 3:
		you.loc = Location(you.loc.x - x, you.loc.y)
	
def moveDist(var):
	retVal = 1
	try:
		print(len(var))
		if var[2] != '':
			retVal = int(var[2])
	except ValueError:
		retVal = 0
	return retVal
	
def inputValidation(var):
	outVal = -1
	
	if var[0] == 'quit':
		outVal = 0
	elif var[0] == 'move' or var[0] == 'walk':
		if var[1] == 'forward':
			outVal = 1
	elif var[0] == 'turn':
		if var[1] == 'left':
			outVal = 2
		elif var[1] == 'right':
			outVal = 3
		elif var[1] == 'around':
			outVal = 4
	elif var[0] == 'compass':
		outVal = 5
			
	return outVal
	
main()


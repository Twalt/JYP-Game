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
		items = generateItems()
		
		while valid:
			print(you.loc)
			var = input("What would you like to do? : ")
			command = var.split(' ')
			if command[0] == 'quit':
				valid = False
					
			events = dict()
			events['quit'] = doQuit
			events['turn'] = doTurn
			events['move'] = doMove
			events['walk'] = doMove
			events['compass'] = doCompass
			
			for key in events:
				if command[0] == key:
					doThis = events[key]
					valid = doThis(you, *command)
			
			if you.compass.direction < 0:
				you.compass.direction += 4
			elif you.compass.direction > 3:
				you.compass.direction -= 4
				
	except KeyboardInterrupt:
		print("\nQuitting")

def doQuit(*extras):
	return False
	
def doTurn(you, command, way, *extras):
	if way == 'left':
		you.compass.direction -= 1
	elif way == 'right':
		you.compass.direction += 1
	elif way == 'around':
		you.compass.direction += 2
	return True

def doMove(you, *command):
	x = 1
	try:
		print(len(command))
		if len(command) >2:
			if command[2] != '':
				x = int(command[2])
	except ValueError:
		x = 0
	if x == 0:
		print("Invalid move distance")
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
	return True
	
def doCompass(you, *extras):
	print("You are facing " + str(you.compass) + ".")
	return True

	
def generateItems():
	retItems = [armor.helm(), armor.boots(), armor.gauntlets(), 
				armor.legplates(), armor.shoulderplates(), 
				armor.breastplate()]
	for i in retItems:
		xVal = random.randint(1, 49)
		yVal = random.randint(1, 22)
		i.loc = Location(xVal, yVal)
	
main()


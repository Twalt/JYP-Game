#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 Arjun <Arjun@HYPERION>
#
from character import Character
from character import Compass
from obstacle import Landmark
from obstacle import Wall
from weapon import weapon
from item import Location
import random
import armor
import data
import sys

def main():
	try:
		print("Type 'help' for a list of commands!")
		valid = True
		
		#Generates player at default location facing north
		you = Character(Location(25,35), Compass(0))
		obs = generateObstacles()			#creates walls
		landmarks = generateLandmarks()		#creates landmark objects
		for x in range(len(landmarks)-1):
			for y in range(len(landmarks[x])-1):
				obs[x][y] = landmarks[x][y]
		items = generateItems()				#creates item list
		
		while valid:
			try:
				var = raw_input("What would you like to do? : ")
			except NameError:
				var = input("What would you like to do? : ")
				
			command = var.split(' ')
			if command[0] == 'quit':
				valid = False
			
			#this is the event function list		
			events = dict()
			events['quit'] = doQuit
			events['turn'] = doTurn
			events['move'] = doMove
			events['walk'] = doMove
			events['loc'] = doLoc
			events['compass'] = doCompass
			events['look'] = doLook
			events['help'] = doHelp
			
			validCommand = False
			
			#event loop checks input for keys in list
			for key in events:
				if command[0] == key:
					doThis = events[key]
					valid = doThis(you, obs, *command)
					validCommand = True
			
			if not validCommand:
				print("You can't do that right now.")
			
			if you.compass.direction < 0:	#changes dir to valid value
				you.compass.direction += 4
			elif you.compass.direction > 3:
				you.compass.direction -= 4
				
	except KeyboardInterrupt:
		print("\nQuitting")

def doLoc(you, *extras):
	print(you.loc)
	return True

#creates landmark objects based on the location values collected
#from the data.py file
def generateLandmarks():
	landmarks = [[0 for x in range(41)] for x in range(51)] 
	
	#adds boulder coordinates to the array
	for y in [Landmark(Location(t[0], t[1]), 'boulder') for t in data.boulder]:
		landmarks[y.loc.x][y.loc.y] = 'boulder'
		
	#adds first tree coordinates to the array
	for y in [Landmark(Location(t[0], t[1]), 'boulder') for t in data.tree1]:
		landmarks[y.loc.x][y.loc.y] = 'dead tree'
		
	#adds second tree coordinates to the array
	for y in [Landmark(Location(t[0], t[1]), 'boulder') for t in data.tree2]:
		landmarks[y.loc.x][y.loc.y] = 'plagued tree'
		
	#adds third tree coordinates to the array
	for y in [Landmark(Location(t[0], t[1]), 'boulder') for t in data.tree3]:
		landmarks[y.loc.x][y.loc.y] = 'charred tree'
		
	#adds fence coordinates to the array
	for y in [Landmark(Location(t[0], t[1]), 'boulder') for t in data.fence]:
		landmarks[y.loc.x][y.loc.y] = 'broken fence gate'
		
	#adds outhouse coordinates to the array
	for y in [Landmark(Location(t[0], t[1]), 'boulder') for t in data.outhouse]:
		landmarks[y.loc.x][y.loc.y] = 'smelly boarded-up outhouse'
		
	#adds chest coordinates to the array
	for y in [Landmark(Location(t[0], t[1]), 'boulder') for t in data.chest]:
		landmarks[y.loc.x][y.loc.y] = 'mysterious locked chest'
		
	#adds cow coordinates to the array
	for y in [Landmark(Location(t[0], t[1]), 'boulder') for t in data.cow]:
		landmarks[y.loc.x][y.loc.y] = 'very stubborn cow'
		
	#adds house coordinates to the array
	for y in [Landmark(Location(t[0], t[1]), 'boulder') for t in data.house]:
		landmarks[y.loc.x][y.loc.y] = 'sinister looking house'
	
	return landmarks
		
#creates walls between the predetermined boundaries
def generateObstacles():
	obs = [[0 for x in range(41)] for x in range(51)] 
	for x in range (0, 50):
		obs[x][0] = 'wall'	
		obs[x][40] = 'wall'
	for y in range(0, 40):
		obs[0][y] = 'wall'
		obs[50][y] = 'wall'
	return obs

#prints lines from help file 
def doHelp(*extras):
	f = open('help.txt')
	lines = f.readlines()
	f.close
	for l in lines:
		print(l.rstrip("\n"))
	
	return True

#prints out objects in adjacent locations
def doLook(you, obs, command, *extras):
	direction = 0
	#there is something after look
	if len(extras) > 0:
		#if told to look left
		if extras[0] == 'left':	
			direction = 1
			#North
			if you.compass.direction == 0:
				if obs[you.loc.x-1][you.loc.y] != '':
					encountered = obs[you.loc.x-1][you.loc.y]
			#East
			elif you.compass.direction == 1:
				if obs[you.loc.x][you.loc.y-1] != '':
					encountered = obs[you.loc.x][you.loc.y-1]
			#South
			elif you.compass.direction == 2:
				if obs[you.loc.x+1][you.loc.y] != '':
					encountered = obs[you.loc.x+1][you.loc.y]
			#West
			elif you.compass.direction == 3:
				if obs[you.loc.x][you.loc.y+1] != '':
					encountered = obs[you.loc.x][you.loc.y+1]	
		#if told to look left	
		elif extras[0] == 'right':
			direction = 2
			#North
			if you.compass.direction == 0:
				if obs[you.loc.x+1][you.loc.y] != '':
					encountered = obs[you.loc.x+1][you.loc.y]
			#East
			elif you.compass.direction == 1:
				if obs[you.loc.x][you.loc.y+1] != '':
					encountered = obs[you.loc.x][you.loc.y+1]
			#South
			elif you.compass.direction == 2:
				if obs[you.loc.x-1][you.loc.y] != '':
					encountered = obs[you.loc.x-1][you.loc.y]
			#West
			elif you.compass.direction == 3:
				if obs[you.loc.x][you.loc.y-1] != '':
					encountered = obs[you.loc.x][you.loc.y-1]	
					
	if encountered != 0:
		if direction == 1:
			print("There is a",encountered,"to the left of you.")
		else:
			print("There is a",encountered,"to the right of you.")
	else:
		if direction == 1:
			print("There is nothing to the left of you.")
		else:
			print("There is nothing to the right of you.")
		
	return True
			
def doQuit(*extras):
	return False
	
def doTurn(you, obs, command, way, *extras):
	if way == '':
		print("You must specify a direction.")
	elif way == 'left':
		you.compass.direction -= 1
	elif way == 'right':
		you.compass.direction += 1
	elif way == 'around':
		you.compass.direction += 2
	else:
		print("You can't turn that way.")
	return True

def doMove(you, obs, *command):
	x = 1
	try:
		if len(command) >2:
			if command[2] != '':
				#value of move distance
				x = int(command[2])
	except ValueError:
		x = 0
	if x == 0:
		print("Invalid move distance")
		
	if x > 0:
		canMove = True
	else:
		canMove = False
		
	counter = 0
	
	#moves forward in increments of 1
	while canMove:
		counter += 1
		
		validLoc = 0
		if len(command) >1:
			if command[1] != "forward":
				validLoc = 3
				x = 0
		else:
			validLoc = 3
			x = 0
			
		#creates a location object based on the compass, one spot away
		#North
		if you.compass.direction == 0:
			newloc = Location(you.loc.x, you.loc.y - 1)
		#East
		elif you.compass.direction == 1:
			newloc = Location(you.loc.x + 1, you.loc.y)
		#South
		elif you.compass.direction == 2:
			newloc = Location(you.loc.x, you.loc.y + 1)
		#West
		elif you.compass.direction == 3:
			newloc = Location(you.loc.x - 1, you.loc.y)
	
		if obs[newloc.x][newloc.y] != 0:
			encountered = obs[newloc.x][newloc.y]
			if x > 1:
				validLoc = 2
			else:
				validLoc = 1
			canMove = False
				
		if counter == x+1:
			canMove = False
		if canMove:
			you.loc = newloc
	
	if validLoc == 2:
		print("You walked %d and encountered a %s" % (counter-1, encountered))
		
	if validLoc == 1:
		print("There is a %s in your way" % (encountered))
	elif validLoc == 3:
		print("You must specify a direction! Only forward works!")
	
	return True
	
def doCompass(you, *extras):
	print("You are facing " + str(you.compass) + ".")
	return True
	
def generateItems():
	retItems = [armor.helm(), armor.boots(), armor.gauntlets(), 
				armor.legplates(), armor.shoulderplates(), 
				armor.breastplate()]
	for i in retItems:
		xVal = random.randint(1, 51)
		yVal = random.randint(1, 41)
		i.loc = Location(xVal, yVal)
	return retItems
	
main()


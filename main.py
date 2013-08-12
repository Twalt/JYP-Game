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
		Landmarks = generateLandmarks()		#creates landmark objects
		obstacles = [obs]					#creates array of obstacles
		for l in Landmarks:
			obstacles.append(l)		#adds landmarks loc to wall loc list
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
					valid = doThis(you, obstacles, *command)
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
	blder = [Landmark(Location(t[0], t[1]), 'boulder') 
		for t in data.boulder]
	tree1 = [Landmark(Location(t[0], t[1]), 'dead tree') 
		for t in data.tree1]
	tree2 = [Landmark(Location(t[0], t[1]), 'plagued tree') 
		for t in data.tree2]
	tree3 = [Landmark(Location(t[0], t[1]), 'charred tree') 
		for t in data.tree3]
	fence = [Landmark(Location(t[0], t[1]), 'broken fence gate') 
		for t in data.fence]
	ouths = [Landmark(Location(t[0], t[1]), 'smelly boarded-up outhouse') 
		for t in data.outhouse]
	chest = [Landmark(Location(t[0], t[1]), 'mysterious locked chest') 
		for t in data.chest]
	cow = [Landmark(Location(t[0], t[1]), 'very stubborn cow') 
		for t in data.cow]
	house = [Landmark(Location(t[0], t[1]),'sinister looking house')
		for t in data.house]
	return [blder, tree1, tree2, tree3, fence, ouths, chest, cow, house]
		
#creates walls between the predetermined boundaries
def generateObstacles():
	obs = [Wall(Location(51, 41))]
	for x in range (0, 51):
		obs.append(Wall(Location(x, 0)))
		obs.append(Wall(Location(x, 41)))
	for y in range(1, 41):
		obs.append(Wall(Location(0, y)))
		obs.append(Wall(Location(51, y)))
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
def doLook(you, obstacles, command, *extras):
	retVal = 0
	#there is something after look
	if len(extras) > 0:
		#if told to look left
		if extras[0] == 'left':	
			#for all each obstacle
			for d in obstacles:
				#for each part of each obstacle
				for o in d:
					#North
					if you.compass.direction == 0:
						if you.loc.x - 1 == o.loc.x:
							if you.loc.y == o.loc.y:
								encountered = o
								retVal = 1
					#East
					elif you.compass.direction == 1:
						if you.loc.y - 1 == o.loc.y:
							if you.loc.x == o.loc.x:
								encountered = o
								retVal = 1
					#South
					elif you.compass.direction == 2:
						if you.loc.x + 1 == o.loc.x:
							if you.loc.y == o.loc.y:
								encountered = o
								retVal = 1
					#West
					elif you.compass.direction == 3:
						if you.loc.y + 1 == o.loc.y:
							if you.loc.x == o.loc.x:
								encountered = o
								retVal = 1
				if retVal == 0:
					retVal = 3		
		#if told to look left	
		elif extras[0] == 'right':
			#for all each obstacle
			for d in obstacles:
				#for each part of each obstacle
				for o in d:
					#North
					if you.compass.direction == 0:
						if you.loc.x + 1 == o.loc.x:
							if you.loc.y == o.loc.y:
								encountered = o
								retVal = 2
					#East
					elif you.compass.direction == 1:
						if you.loc.y + 1 == o.loc.y:
							if you.loc.x == o.loc.x:
								encountered = o
								retVal = 2
					#South
					elif you.compass.direction == 2:
						if you.loc.x - 1 == o.loc.x:
							if you.loc.y == o.loc.y:
								encountered = o
								retVal = 2
					#West
					elif you.compass.direction == 3:
						if you.loc.y - 1 == o.loc.y:
							if you.loc.x == o.loc.x:
								encountered = o
								retVal = 2
				if retVal == 0:
					retVal = 4			
	if retVal == 1:
		print("There is a",encountered,"to the left of you.")
	elif retVal == 2:
		print("There is a",encountered,"to the right of you.")
	elif retVal == 3:
		print("There is nothing to the left of you.")
	elif retVal == 4:
		print("There is nothing to the right of you.")
		
	return True
			
def doQuit(*extras):
	return False
	
def doTurn(you, obstacles, command, way, *extras):
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

def doMove(you, obstacles, *command):
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
		
		#for each obstacle 
		for d in obstacles:
			#for each location in each obstacle
			for o in d:
				#if the new location interferes with an existing location
				if o.loc == newloc:
					encountered = o
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
		print("You walked %d and encountered a %s" % (counter-1, encountered.toStr()))
		
	if validLoc == 1:
		print("There is a %s in your way" % (encountered.toStr()))
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


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
		you = Character(Location(25,35), Compass(0))
		obs = generateObstacles()
		Landmarks = generateLandmarks()
		obstacles = [obs]
		for l in Landmarks:
			obstacles.append(l)
		items = generateItems()
		
		while valid:
			try:
				var = raw_input("What would you like to do? : ")
			except NameError:
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
			events['look'] = doLook
			events['help'] = doHelp
			
			validCommand = False
			
			for key in events:
				if command[0] == key:
					doThis = events[key]
					valid = doThis(you, obstacles, *command)
					validCommand = True
			
			if not validCommand:
				print("You can't do that right now.")
			
			if you.compass.direction < 0:
				you.compass.direction += 4
			elif you.compass.direction > 3:
				you.compass.direction -= 4
				
	except KeyboardInterrupt:
		print("\nQuitting")

def generateLandmarks():
	boulder = [Landmark(Location(t[0], t[1]), 'boulder') 
		for t in data.boulder]
	tree1 = [Landmark(Location(t[0], t[1]), 'dead tree') 
		for t in data.tree1]
	tree2 = [Landmark(Location(t[0], t[1]), 'plagued tree') 
		for t in data.tree2]
	tree3 = [Landmark(Location(t[0], t[1]),'charred tree') 
		for t in data.tree3]
	fence = [Landmark(Location(t[0], t[1]),'broken fence gate') 
		for t in data.fence]
	outh = [Landmark(Location(t[0], t[1]),'smelly boarded-up outhouse') 
		for t in data.outhouse]
	chest = [Landmark(Location(t[0], t[1]),'mysterious locked chest') 
		for t in data.chest]
	cow = [Landmark(Location(t[0], t[1]),'very stubborn cow') 
		for t in data.cow]
	return [boulder, tree1, tree2, tree3, fence, outh, chest, cow]			
		
def generateObstacles():
	obs = [Wall(Location(51, 41))]
	for x in range (0, 51):
		obs.append(Wall(Location(x, 0)))
		obs.append(Wall(Location(x, 41)))
	for y in range(1, 41):
		obs.append(Wall(Location(0, y)))
		obs.append(Wall(Location(51, y)))
	return obs

def doHelp(*extras):
	f = open('help.txt')
	lines = f.readlines()
	f.close
	for l in lines:
		print(l.rstrip("\n"))
	
	return True

def doLook(you, obstacles, command, *extras):
	retVal = 0
	if len(extras) > 0:
		if extras[0] == 'left':	
			
			for d in obstacles:
				for o in d:
					#North
					if you.compass.direction == 0:
						if you.loc.x - 1 == o.loc.x:
							if you.loc.y == o.loc.y:
								print(o.loc)
								retVal = 1
					#East
					elif you.compass.direction == 1:
						if you.loc.y - 1 == o.loc.y:
							if you.loc.x == o.loc.x:
								print(o.loc)
								retVal = 1
					#South
					elif you.compass.direction == 2:
						if you.loc.x + 1 == o.loc.x:
							if you.loc.y == o.loc.y:
								print(o.loc)
								retVal = 1
					#West
					elif you.compass.direction == 3:
						if you.loc.y + 1 == o.loc.y:
							if you.loc.x == o.loc.x:
								print(o.loc)
								retVal = 1
				if retVal == 0:
					retVal = 3			
		elif extras[0] == 'right':
			for d in obstacles:
				for o in d:
					#North
					if you.compass.direction == 0:
						if you.loc.x + 1 == o.loc.x:
							if you.loc.y == o.loc.y:
								retVal = 2
					#East
					elif you.compass.direction == 1:
						if you.loc.y + 1 == o.loc.y:
							if you.loc.x == o.loc.x:
								retVal = 2
					#South
					elif you.compass.direction == 2:
						if you.loc.x - 1 == o.loc.x:
							if you.loc.y == o.loc.y:
								retVal = 2
					#West
					elif you.compass.direction == 3:
						if you.loc.y - 1 == o.loc.y:
							if you.loc.x == o.loc.x:
								retVal = 2
				if retVal == 0:
					retVal = 4			
	if retVal == 1:
		print("There is a wall to the left of you.")
	elif retVal == 2:
		print("There is a wall to the right of you.")
	elif retVal == 3:
		print("There is nothing to the left of you.")
	elif retVal == 4:
		print("There is nothing to the right of you.")
		
	return True
			
def doQuit(*extras):
	return False
	
def doTurn(you, obstacles, command, way, *extras):
	if way == 'left':
		you.compass.direction -= 1
	elif way == 'right':
		you.compass.direction += 1
	elif way == 'around':
		you.compass.direction += 2
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
	
	while canMove:
		#increment counter
		#check if obstacle
		#move forward 1
		#
		counter += 1
			
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
		
		validLoc = 0
		if len(command) >1:
			if command[1] != "forward":
				validLoc = 3
				x = 0
		else:
			validLoc = 3
			x = 0
			
		
		for d in obstacles:
			for o in d:
				if o.loc == newloc:
					encountered = o
					if x > 1:
						validLoc = 2
					else:
						validLoc = 1
					canMove = False
		
		if o.loc == newloc:
			validLoc = 2
			you.loc = newloc
		if counter == x:
			canMove = False
		if canMove:
			you.loc = newloc
	
	if validLoc == 2:
		print("You walked %d and encountered a %s" % (counter-1, encountered.toStr()))
		
	if validLoc == 1:
		print("There is a", encountered, "in your way")
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


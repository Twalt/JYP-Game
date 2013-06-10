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
import sys

def main():
	try:
		print("Type 'help' for a list of commands!")
		valid = True
		you = Character(Location(25,35), Compass(0))
		obstacles = generateObstacles()
		Landmarks = generateLandmarks()
		items = generateItems()
		
		while valid:
			print(you.loc)
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
	boulder = [Landmark(Location(5, 24), 'boulder'), 
				Landmark(Location(4, 25), 'boulder'), 
				Landmark(Location(5, 25), 'boulder'), 
				Landmark(Location(4, 26), 'boulder'), 
				Landmark(Location(5, 26), 'boulder'), 
				Landmark(Location(6, 26), 'boulder'), 
				Landmark(Location(5, 27), 'boulder'), 
				Landmark(Location(6, 27), 'boulder'), 
				Landmark(Location(6, 28), 'boulder'), 
				Landmark(Location(6, 29), 'boulder')]
	tree1 = [Landmark(Location(11, 34), 'dead tree'),
				Landmark(Location(10, 35), 'dead tree'),
				Landmark(Location(11, 35), 'dead tree'),
				Landmark(Location(12, 35), 'dead tree'),
				Landmark(Location(11, 36), 'dead tree')]
	tree2 = [Landmark(Location(15, 12), 'dead tree'),
				Landmark(Location(14, 13), 'dead tree'),
				Landmark(Location(15, 13), 'dead tree'),
				Landmark(Location(16, 13), 'dead tree'),
				Landmark(Location(15, 14), 'dead tree')]
	tree3 = [Landmark(Location(42, 16), 'dead tree'),
				Landmark(Location(41, 17), 'dead tree'),
				Landmark(Location(42, 17), 'dead tree'),
				Landmark(Location(43, 17), 'dead tree'),
				Landmark(Location(42, 18), 'dead tree')]
	fence = [Landmark(Location(13, 4), 'broken fence'),
				Landmark(Location(15, 4), 'broken fence'),
				Landmark(Location(17, 4), 'broken fence'),
				Landmark(Location(19, 4), 'broken fence'),
				Landmark(Location(21, 4), 'broken fence'),
				Landmark(Location(22, 4), 'broken fence'),
				Landmark(Location(22, 5), 'broken fence'),
				Landmark(Location(23, 5), 'broken fence'),
				Landmark(Location(23, 6), 'broken fence'),
				Landmark(Location(25, 6), 'broken fence gate'),
				Landmark(Location(27, 6), 'broken fence'),
				Landmark(Location(30, 6), 'broken fence'),
				Landmark(Location(31, 6), 'broken fence'),
				Landmark(Location(33, 6), 'broken fence'),
				Landmark(Location(39, 6), 'broken fence'),
				Landmark(Location(41, 6), 'broken fence'),
				Landmark(Location(41, 8), 'broken fence'),
				Landmark(Location(41, 9), 'broken fence'),
				Landmark(Location(41, 11), 'broken fence'),
				Landmark(Location(41, 13), 'broken fence'),
				Landmark(Location(42, 13), 'broken fence'),
				Landmark(Location(42, 14), 'broken fence'),
				Landmark(Location(43, 14), 'broken fence'),
				Landmark(Location(43, 15), 'broken fence'),
				Landmark(Location(43, 16), 'broken fence'),
				Landmark(Location(43, 18), 'broken fence'),
				Landmark(Location(43, 19), 'broken fence'),
				Landmark(Location(43, 21), 'broken fence'),
				Landmark(Location(43, 23), 'broken fence'),
				Landmark(Location(43, 25), 'broken fence'),
				Landmark(Location(43, 27), 'broken fence'),
				Landmark(Location(45, 27), 'broken fence'),
				Landmark(Location(47, 27), 'broken fence'),
				Landmark(Location(48, 27), 'broken fence')]
	outhouse = [Landmark(Location(36, 6), 'smelly boarded-up outhouse'),
				Landmark(Location(37, 6), 'smelly boarded-up outhouse'),
				Landmark(Location(38, 6), 'smelly boarded-up outhouse'),
				Landmark(Location(36, 7), 'smelly boarded-up outhouse'),
				Landmark(Location(37, 7), 'smelly boarded-up outhouse'),
				Landmark(Location(38, 7), 'smelly boarded-up outhouse'),
				Landmark(Location(36, 8), 'smelly boarded-up outhouse'),
				Landmark(Location(37, 8), 'smelly boarded-up outhouse'),
				Landmark(Location(38, 8), 'smelly boarded-up outhouse')]
	chest = [Landmark(Location(45, 36), 'mysterious locked chest'),
				Landmark(Location(46, 36), 'mysterious locked chest'),
				Landmark(Location(47, 36), 'mysterious locked chest'),
				Landmark(Location(45, 37), 'mysterious locked chest'),
				Landmark(Location(46, 37), 'mysterious locked chest'),
				Landmark(Location(47, 37), 'mysterious locked chest')]
	cow = [Landmark(Location(13, 19), 'stubborn cow'),
				Landmark(Location(14, 19), 'stubborn cow'),
				Landmark(Location(13, 20), 'stubborn cow'),
				Landmark(Location(14, 20), 'stubborn cow'),
				Landmark(Location(13, 21), 'stubborn cow'),
				Landmark(Location(14, 21), 'stubborn cow'),
				Landmark(Location(13, 22), 'stubborn cow'),
				Landmark(Location(14, 22), 'stubborn cow')]
	return [boulder, tree1, tree2, tree3, fence, outhouse, chest, cow]			
		

def generateObstacles():
	obs = [Wall(Location(51, 41))]
	for x in range (0, 53):
		obs.append(Wall(Location(x, 0)))
		obs.append(Wall(Location(x, 41)))
	for y in range(1, 40):
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

def doLook(you, obstacles, command, way, *extras):
	retVal = 0
	if way == 'left':	
		for o in obstacles:
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
	elif way == 'right':
		for o in obstacles:
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
				x = int(command[2])
	except ValueError:
		x = 0
	if x == 0:
		print("Invalid move distance")
	#North
	if you.compass.direction == 0:
		newloc = Location(you.loc.x, you.loc.y - x)
	#East
	elif you.compass.direction == 1:
		newloc = Location(you.loc.x + x, you.loc.y)
	#South
	elif you.compass.direction == 2:
		newloc = Location(you.loc.x, you.loc.y + x)
	#West
	elif you.compass.direction == 3:
		newloc = Location(you.loc.x - x, you.loc.y)
	
	validLoc = 0
	moveVal = 0
	if len(command) >1:
		if command[1] != "forward":
			validLoc = 3
			x = 0
	else:
		validLoc = 3
		x = 0
		
		
	for o in obstacles:
		if o.loc == newloc:
			validLoc = 1
	if x > 1:
		if o.loc == newloc:
			moveVal = x-1
			validLoc = 2
			you.loc = newloc
		elif newloc.x >50:
			moveVal = 50 - you.loc.x
			newloc.x = 50
			validLoc = 2
		elif newloc.x <0:
			moveVal = you.loc.x
			newloc.x = 0
			validLoc = 2
		elif newloc.y >40:
			moveVal = 40 - you.loc.y
			newloc.y = 40
			validLoc = 2
		elif newloc.y <0:
			moveVal = you.loc.y
			newloc.y = 0
			validLoc = 2
	
	if validLoc == 2:
		print("You walked %d and encountered a wall" % (moveVal))
		
	if validLoc == 1:
		print("There is a wall in your way")
	elif validLoc == 3:
		print("You must specify a direction! Only forward works!")
	else:
		you.loc = newloc
	
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


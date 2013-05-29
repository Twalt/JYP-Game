#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 Arjun <Arjun@HYPERION>
#  
#  
from weapon import weapon
from item import Location
from character import Character
import armor
def main():
	y = Character(Location(45,4))
	z = armor.helm(Location(2,2))
	y.helm = z
	y.helm.setLoc(Location(-2,-2))
	f = weapon(Location(1, 1))
	print(f.loc)
	print(z.loc)
	print(y.helm.loc)
	print(f.loc)
	return 0

main()


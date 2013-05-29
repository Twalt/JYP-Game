#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 Arjun <Arjun@HYPERION>
#  
#  
import weapon
import location
loc = location.Location(1, 1)
def main():
	f = weapon.weapon()
	f.setCoord(loc)
	print(f.getCoord())
	return 0

main()


#!/usr/bin/python3
#-*- coding: utf-8 -*-
import re
import os
import sys

with open("ex-2.pkl", "r") as file:
	fd = file.readlines()
output = open("test.txt", "w")
output.write("COM=\n"+"CHARGE=\n"+"\n")
i=0
for line in fd[1:]:
	if len(line.split(" ")) == 3:
		i+=1
		output.write("BEGIN IONS\n"+"TITLE=ex-2.pkl."+str(i)+"\nPEPMASS="+line+"CHARGE="+line.rstrip("\n").split(" ")[2]+"+\n")
	elif len(line.split(" ")) == 2:
		output.write(line.rstrip(" ?\n")
	elif len(line.split(" ")) == 1:
		output.write("END IONS\n\n")
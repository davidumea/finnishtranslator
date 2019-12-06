#!/usr/bin/python

import os
import subprocess

print('1: Translate a file')
print('2: Translate a text input')
method = input('Choose translation method (1 or 2): ')

rules = [['g','k'],['k','kk'],['b','p'],['i','ii'],['å','ä'],['d','t'],['a','ai'],['e','ei'],['meit','saatana'],['jaikk','saatana']]

def fileInput():
	with open(filePath,'r') as file:
		fileData = file.read()

	for rule in rules:
		fileData = fileData.replace(rule[0],rule[1])

	print(fileData)

def textInput():
	fileData = text.lower()

	for rule in rules:
		fileData = fileData.replace(rule[0],rule[1])

	print(fileData)


if method == '1':
	subprocess.call(['ls','-a'])
	filePath = input('Path to file to read from: ')
	fileInput()

elif method == '2':
	text = input('Enter text to translate: ')
	textInput()

else:
	print('Error: Please press 1 or 2 to choose a calculation method')

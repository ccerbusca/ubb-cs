import re
import os
from math import sqrt

l = []

def getReal(cn):
	#return cn[0]
	return cn["Re"]

def getImag(cn):
	#return cn[1]
	return cn["Im"]

def createComplexNr(real, imag):
	l.append({"Re" : real, "Im" : imag})

def main_menu(menu):
	for i in range(1, len(menu) + 1):
		print("{}. {}".format(i, menu[i][0]))
	try:
		menu[int(input())][1]()
	except ValueError:
		print("Please enter a valid option")
		input()
		startProgram()

def readList():
	clear()
	read = True
	print("Introduce the complex numbers one at a time in the following form: a + bi")
	while read == True:
		string = input()
		compNr = re.search(r"([-]?\d+)[ ]?[+][ ]?([-]?\d+)i", string) #using a regular expression to filter out the input and get the real and imaginary parts from a string
		if (compNr != None): #if no real and imaginary parts were found, stop reading
			createComplexNr(int(compNr.group(1)), int(compNr.group(2)))
		else:
			read = False
	startProgram()

def modulus(li):
	'''
	The following function calculates the modulus of the specified complex number:
		|a + bi| = sqrt(a * a + b * b)
	'''
	return (getReal(li) ** 2 + getImag(li) ** 2)**(1/2)

def calcLongestSequenceIncreasingModulus():
	start = 0
	end = 0
	maxStart = 0
	maxEnd = 0
	i = 0
	while i < len(l) - 1:
		if modulus(l[i]) < modulus(l[i + 1]):
			start = i
			i += 1
			while i < len(l) - 1 and modulus(l[i]) < modulus(l[i + 1]):
				i += 1
			end = i
			if end - start > maxEnd - maxStart:
				maxStart = start
				maxEnd = end
		else:
			i += 1
	return maxStart, maxEnd

def calcLongestSequenceSum10():
	start = 0
	end = 0
	maxStart = 0
	maxEnd = 0
	i = 0
	while i < len(l):
		j = i
		sum = [0, 0]
		while j < len(l) and (sum[0] < 10 or sum[1] < 10):
			sum[0] += getReal(l[j])
			sum[1] += getImag(l[j])
			j += 1
		if sum[0] == 10 and sum[1] == 10 and j - i - 1 > maxEnd - maxStart:
			maxStart = i
			maxEnd = j - 1
		i += 1
	return maxStart, maxEnd

def longestSequenceIncreasingModulus():
	start, end = calcLongestSequenceIncreasingModulus()
	printLongestSequence(start, end)

def longestSequenceSum10():
	start, end = calcLongestSequenceSum10()
	printLongestSequence(start, end)

def printList():
	clear()
	for i in l:
		print("{} + {}i".format(getReal(i), getImag(i)))
	input("\nPress any key to return to menu")
	startProgram()

def printLongestSequence(start, end):
	clear()
	print("The longest sequence with the specified property is:")
	for i in l[start:end + 1]:
		print("{} + {}i".format(getReal(i), getImag(i)))
	input("\nPress any key to return to menu")
	startProgram()

def exit():
	pass

menu = {1: ["Read a list of complex numbers (in z = a + bi form) from the keyboard.", readList],
		2: ["Print the entire list of numbers.", printList],
		3: ["Longest sequence having numbers with increasing modulus.", longestSequenceIncreasingModulus],
		4: ["Longest sequence where both real and imaginary parts of the number can be written with the same digits", longestSequenceSum10],
		5: ["Exit the application.", exit]}

clear = lambda: os.system("cls") #assigning a lambda function that clears the console window

def startProgram():
	clear()
	main_menu(menu)

createComplexNr(1, 2)
createComplexNr(3, 4)
createComplexNr(5, 6)
createComplexNr(11, 20)
createComplexNr(1, 0)
createComplexNr(2, 0)
createComplexNr(2, -2)
createComplexNr(-2, 2)
createComplexNr(3, 1)
createComplexNr(4, 2)
createComplexNr(0, 3)
createComplexNr(0, 4)
startProgram()

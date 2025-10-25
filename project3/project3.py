"""
Programming Assignment 3: Cryptography
Author: Geremy Giles
Date: 10/24/2025
Description: A program to encrypt and decrypt a user-inputted message using the Hill Cipher method.
"""

#### Imports ####
import numpy as np

#### Definitions ####
global file_path
global file_contents
rows = 0
columns = 0
selected_menu_option = -1
matrix1 = []
matrix2 = []
scalar = None


#### Functions ####

def prompt_file_name():
	# Request file name from user
	print("Please input the name of the text file containing the message. (Omit the \".txt\")")

	# Validate user input with loop
	global file_path
	file_path = ""
	while file_path == "": # Check for valid input
		try:
			inputted_file_name = input("File Name: ").strip()
			if inputted_file_name == "":
				print("No input entered.") # Print error message
			else:
				file_path = inputted_file_name + ".txt"
		except:
			print("Invalid entry") # Print error message
	
	# Print file path
	print("Inputted file path: " + file_path)

def read_file():
	global file_path
	global file_contents

	file_contents = ""
	while file_contents == "": # Check for valid input
		try:
			with open(file_path, 'r') as file:
				file_contents = file.read()
				print("File Content: " + file_contents)
		except FileNotFoundError:
			print("File cannnot be found. Please check the file name and try again.\n")
			prompt_file_name()

#### Main Code ####

# Print title
print("Part 1: Encrypting")

# Prompt for file name
prompt_file_name()
read_file()
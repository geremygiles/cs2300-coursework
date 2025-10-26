"""
Programming Assignment 3: Cryptography
Author: Geremy Giles
Date: 10/24/2025
Description: A program to encrypt and decrypt a user-inputted message using the Hill Cipher method.
"""

#### Imports ####
import math
import numpy as np

#### Definitions ####
rows = 0
columns = 0
selected_menu_option = -1
matrix1 = []
matrix2 = []
scalar = None


#### Functions ####

### Function for prompting user for file name
def prompt_file_name():
	# Request file name from user
	print("Please input the name of the text file containing the message. (Omit the \".txt\")")

	# Validate user input with loop
	file_path = ""
	while file_path == "":
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

	# Pass file path to read file function
	read_file(file_path)



### Function for reading file contents
def read_file(path):
	file_contents = ""
	while file_contents == "": # Check for valid file path
		# Try to open file with given path
		try:
			with open(path, 'r') as file:
				file_contents = file.read()
				print("File Content: " + file_contents)
		except FileNotFoundError:
			print("File cannnot be found. Please check the file name and try again.\n") # Print error message
			prompt_file_name()

	# Pass file contents to create matrix function
	create_matrix(file_contents)



### Function for creating a 4xj matrix from file contents
def create_matrix(contents):
	# Create a matrix
	matrix = []

	# Calculate number of columns needed based on length of contents
	print("Length of contents: " + str(len(contents)))
	columns = math.ceil(float(len(contents)) / 4.0)
	print("Number of columns needed: " + str(columns))

	# Break contents into list
	contents_list = list(contents.strip())
	print("Contents List: " + str(contents_list))

	for i in range(len(contents_list)):
		contents_list[i] = ord(contents_list[i])

	# Fill matrix by column, with 4 elements per column
	for i in range(columns):
		column = []
		for i in range(4):
			if len(contents_list) > 0:
				column.append(contents_list.pop(0))
			else:
				column.append(0) # Padding character if contents run out
		matrix.append(column)
	
	# Convert to numpy matrix
	np_matrix = np.asmatrix(matrix)
	print("NP Matrix: \n")
	print(np_matrix)
	print(np_matrix.T)
		#	row = []
		#	for j in range(columns):
		#		while True:
		#			try:
		#				value = int(input(f"Enter value for position ({i+1},{j+1}): "))
		#				row.append(value)
		#				break
		#			except ValueError:
		#				print("Invalid input. Please enter an integer.")
		#	matrix.append(row)
		#return matrix

#### Main Code ####

# Print title
print("Part 1: Encrypting")

# Prompt for file name
prompt_file_name()
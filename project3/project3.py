"""
Programming Assignment 3: Cryptography
Author: Geremy Giles
Date: 10/24/2025
Description: A program to encrypt and decrypt a user-inputted message using the Hill Cipher method.
"""

#### Imports ####
import math
from tkinter import E
import numpy as np

#### Definitions ####
rows = 0
columns = 0
selected_menu_option = -1
matrix1 = []
matrix2 = []
scalar = None

matrix_a = [[1, 2, -2, 3], [-1, -3, -1, -3], [-1, -5, -2, -1], [1, 4, 2, 2]]
np_matrix_a = np.asmatrix(matrix_a)


#### Functions ####

### Function for prompting user for file name
### Returns the properly formatted file path
def open_file():
	# Request file name from user
	print("Please input the name of the text file containing the message. (Omit the \".txt\")")

	# Validate user input with loop
	while True:
		inputted_file_name = input("File Name: ").strip()
		if inputted_file_name == "":
			print("No input entered.\n") # Print error message
		else:
			file_path = inputted_file_name + ".txt" # Append the '.txt' extension
			try:
				with open(file_path, 'r') as file: # Attempt to open file
					file_contents = read_file(file_path) # Read file with given path
					return file_contents
			except FileNotFoundError:
				print(f"'{file_path}' cannnot be found. Please check the file name and try again.\n")
				continue # Restart loop
			except Exception as e:
				print("The following error occurred: " + str(e) + "\nPlease try again.\n") # Print error message
				continue # Restart loop




### Function for reading file contents
### Takes the file path
### Returns the contents of the file
def read_file(path):
	file_contents = ""
	# Try to open file with given path
	try:
		with open(path, 'r') as file:
			file_contents = file.read()
			return file_contents
	except FileNotFoundError:
		print("File cannnot be found. Please check the file name and try again.\n") # Print error message
		open_file()
	except Exception as e:
		print("The following error occurred: " + str(e) + "\nPlease try again.") # Print error message
		open_file()



### Function for creating a 4xj matrix of Unicode values from file contents
### Takes the contents of the file
### Returns the NumPy Matrix
def create_matrix(contents):
	# Create a matrix
	matrix = []

	# Calculate number of columns needed based on length of contents
	columns = math.ceil(float(len(contents)) / 4.0)

	# Break contents into list
	contents_list = list(contents.strip())

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

	return np_matrix

#### Main Code ####

# Print title
print("Part 1: Encrypting")


file_contents = open_file() # Prompt for file name and read contents
np_matrix_b = create_matrix(file_contents) # Create matrix from file contents
print("\nMatrix B: \n")
print(np_matrix_b.T) # Print the transpose of the matrix for better readability

np_matrix_c = np_matrix_a.T * np_matrix_b.T # Create the encrypted matrix via matrix multiplication (transposed for correct dimensions))
print("\nMatrix C: \n")
print(np_matrix_c)
"""
Programming Assignment 4: Leontief Model
Author: Geremy Giles
Date: 11/16/2025
Description: A program to calculate the total output of an economy using the Leontief input-output model.
"""

#### Imports ####
import numpy as np

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


### Function for creating the 3x3 D matrix and 1x3 E matrix of float values from file contents
### Takes the contents of the file
### Returns the NumPy Matrices
def create_matrices(contents):
	# Create a matrix
	d_matrix = []
	e_matrix = []

	contents_list = contents.strip().split(' ') # Split by spaces

	# Fill D matrix by row, with 3 elements per row
	for i in range(3):
		row = []
		for i in range(3):
			row.append(float(contents_list.pop(0)))
		d_matrix.append(row)

	# Fill E matrix with 3 elements
	for i in range(3):
		e_matrix.append(float(contents_list.pop(0)))
	
	# Convert both to numpy matrices
	np_d_matrix = np.asmatrix(d_matrix)
	np_e_matrix = np.asmatrix(e_matrix)
	np_e_matrix = np_e_matrix.T # Transpose E to make it 3x1
	
	return [np_d_matrix, np_e_matrix]


### Main Code ###

file_contents = open_file() # Prompt for file name and read contents
matrices = create_matrices(file_contents) # Create matrix from file contents
# print("\nD Matrix:")
# print(matrices[0])
# print("\nE Matrix:")
# print(matrices[1])

# Calculate I - D
identity_matrix = np.identity(3) # Create identity matrix
i_minus_d = identity_matrix - matrices[0] # I - D
# print("\n\nI - D Matrix:")
# print(i_minus_d) # Print I - D

# Calculate Inverse of I - D
inverse_i_d = np.linalg.inv(i_minus_d) # Inverse of I - D
# inverse_i_d = inverse_i_d.round(2) # Round to 2 decimal places (used to test with example values provided)
# print("\nInverse of I - D Matrix:")
# print(inverse_i_d)

# Calculate X
x_matrix = inverse_i_d * matrices[1] # X = Inverse(I - D) * E
x_matrix = x_matrix.round(1) # Round to 2 decimal places
print("\nTotal Output (X) Matrix:")
print(x_matrix) # Print X matrix
"""
Programming Assignment 1: Matrix Calculator
Author: Geremy Giles
Date: 09/14/2025
Description: A program to perform fundamental matrix operations, including addition, subtraction, and scalar multiplication.
"""

#### Imports ####
import numpy as np

#### Definitions ####
options = {1: "Addition", 2: "Subtraction", 3: "Scalar Multiplication", 4: "Exit"}
rows = 0
columns = 0
selected_menu_option = -1
matrix1 = []
matrix2 = []
scalar = None


#### Functions ####

def calculator():
	global matrix1
	global matrix2

	# Prompt user for menu option input
	prompt_menu()

	# Prompt user for rows and columns of two matrixes, validate with loop, and store in var
	prompt_rows_columns()

	# Call the fill_matrix function twice to get both matrixes (unless the user selected scalar multiplication)
	matrix1 = fill_matrix(1)

	# Scalar multiplication only requires one matrix, so skip the second matrix
	if selected_menu_option != 3: 
		matrix2 = fill_matrix(2)
	else:
		prompt_scalar()

	# Perform the selected operation
	calculate()

	# Perform the selected operation with NumPy
	calculate_with_numpy()

	# Reset all global variables
	reset_globals()

	# Restart the calculator
	calculator() 

def prompt_menu():
	# List menu options
	print("\n1. Addition" + 
	   "\n2. Subtraction" + 
	   "\n3. Scalar Multiplication" + 
	   "\n4. Exit")

	# Validate user input with loop
	menu_option = -1;
	while menu_option < 1 or menu_option > 4: # Check for valid input
		try:
			menu_option = int(input("Choose an option listed above: ").strip())
			if menu_option < 1 or menu_option > 4:
				print("Invalid entry") # Print error message
		except:
			print("Invalid entry") # Print error message
	
	# Print selected option
	print("You selected " + options[menu_option] + "\n")
	
	global selected_menu_option
	selected_menu_option = menu_option

	if selected_menu_option == 4:
		print("Exiting...")
		exit()

def prompt_rows_columns():
	global rows
	global columns
	rows = 0
	columns = 0

	while rows == 0 or columns == 0:
		try:
			rows_and_columns = input ("Enter the amount of rows and columns in the matrixes, with the following format: “# #”\n").strip()
			# try to find the index of the space character
			space_index = rows_and_columns.index(" ")
			# Splice the string into rows and colums
			rows = int(rows_and_columns[:space_index])
			columns = int(rows_and_columns[space_index+1:])
		except: 
			# No space found or letters entered, reprompt user
			print("Input error")

def fill_matrix(matrix_index):
	# Print a confirmation message and direct to the next matrix
	print("Success!" +
		f"\n\nMatrix {matrix_index}:" +
		f"\nEnter the rows of the {rows}x{columns} matrix:")
	matrix = []
	# start a while loop to iterate until all data has been entered
	iterate_rows = 0
	while iterate_rows < rows: 
		# Verify user input with a loop
		current_row_list = []
		all_integers = False
		while len(current_row_list) != columns or all_integers != True:
			try:
				# Prompt the user for the nth row of the matrix
				current_row = input(f"Row {iterate_rows+1}: ").strip()
				# try to split the input at spaces
				current_row_list = current_row.split(" ")

				# Attempt to change contents to integers
				iterate = 0
				while iterate < len(current_row_list):
					# Remove any extra spaces
					if current_row_list[iterate] == "":
						current_row_list.pop(iterate)
						continue

					current_row_list[iterate] = int(current_row_list[iterate].strip())
					iterate += 1
				all_integers = True
				if len(current_row_list) != columns:
					print("Invalid entry") # Print error message
			except Exception: 
				# User didn’t enter enough data or input other than integer was received, reprompt user
				print("Invalid entry") # Print error message
				all_integers = False
		# Append the current row to the matrix
		matrix.append(current_row_list)
		iterate_rows += 1

	return matrix

def prompt_scalar():
	global scalar

	# Validate user input with loop
	scalar = None;
	while scalar == None: # Check for valid input
		try:
			scalar = int(input("Enter the scalar value: ").strip())
		except:
			print("Invalid entry") # Print error message

def calculate():

	final_matrix = []
	
	row_index = 0 # Iterate through each row
	while row_index < rows: 
		column_index = 0 # Iterate through each column
		row = []
		match selected_menu_option:
			case 1: # Addition
				while column_index < columns:
					row.append(matrix1[row_index][column_index] + matrix2[row_index][column_index])
					column_index += 1
			case 2: # Subtraction
				while column_index < columns:
					row.append(matrix1[row_index][column_index] - matrix2[row_index][column_index])
					column_index += 1
			case 3: # Scalar Multiplication
				while column_index < columns:
					row.append(matrix1[row_index][column_index] * scalar)
					column_index += 1
				
		final_matrix.append(row)
		row_index += 1

	print("\nResult:")
	# Print the final matrix
	print("Matrix:")

	for row in final_matrix:
		formatted_string =  ""
		for item in row:
			formatted_string += str(item) + " "
		print(formatted_string.strip())

def calculate_with_numpy():
	final_matrix = []

	print("\nNumPy:")
	match selected_menu_option:
		case 1: # Addition
			final_matrix = np.add(matrix1, matrix2)
		case 2: # Subtraction
			final_matrix = np.subtract(matrix1, matrix2)
		case 3: # Scalar Multiplication
			final_matrix = np.multiply(matrix1, scalar)

	for row in final_matrix:
		formatted_string =  ""
		for item in row:
			formatted_string += str(item) + " "
		print(formatted_string.strip())

def reset_globals():
	global rows
	global columns
	global selected_menu_option
	global matrix1
	global matrix2
	global scalar
	rows = 0
	columns = 0
	selected_menu_option = -1
	matrix1 = []
	matrix2 = []
	scalar = None


#### Main Code ####

# Print title
print("Matrix Calculator")

# Start the calculator
calculator() 
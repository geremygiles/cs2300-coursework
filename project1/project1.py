"""
Programming Assignment 1: Matrix Calculator
Author: Geremy Giles
Date: 09/14/2025
Description: A program to perform fundamental matrix operations, including addition, subtraction, and scalar multiplication.
"""

#### Functions ####
from sys import exception


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
					print(f"Input error")
			except Exception: 
				# User didn’t enter enough data or input other than integer was received, reprompt user
				print(f"Input error")
				all_integers = False
		# Append the current row to the matrix
		matrix.append(current_row_list)
		iterate_rows += 1

	return matrix

#### Definitions ####
options = {1: "Addition", 2: "Subtraction", 3: "Scalar Multiplication", 4: "Exit"}


#### Main Code ####

# Print title
print("Matrix Calculator")

# List menu options
print("1. Addition" + 
	  "\n2. Subtraction" + 
	  "\n3. Scalar Multiplication" + 
	  "\n4. Exit")

# Prompt user input, validate with loop, and store in var
menu_option = -1;
while menu_option < 1 or menu_option > 4:
	try:
		menu_option = int(input("Choose an option listed above: ").strip())
		if menu_option < 1 or menu_option > 4:
			print("Invalid entry")
	except:
		# Print error message and reprompt user
		print("Invalid entry")
		

# Print selected option
print("You selected " + options[menu_option] + "\n")
# Prompt user for rows and columns of two matrixes, and store in var
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



# Attempt to splice the input into separate integer variables, and throw and error and reprompt if needed

# Call the fill_matrix function twice to get both matrixes
matrix1 = fill_matrix(1)
print(matrix1)
matrix2 = fill_matrix(2)
print(matrix2)

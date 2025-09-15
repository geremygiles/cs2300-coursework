"""
Programming Assignment 1: Matrix Calculator
Author: Geremy Giles
Date: 09/14/2025
Description: A program to perform fundamental matrix operations, including addition, subtraction, and scalar multiplication.
"""


#### Definitions ####
options = {1: "Addition", 2: "Subtraction", 3: "Scalar Multiplication", 4: "Exit"}
rows = 0
columns = 0
selected_menu_option = -1


#### Functions ####

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

def prompt_menu():
	# List menu options
	print("1. Addition" + 
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


#### Main Code ####

# Print title
print("Matrix Calculator")

# Prompt user for menu option input
prompt_menu()

# Prompt user for rows and columns of two matrixes, validate with loop, and store in var
prompt_rows_columns()

# Call the fill_matrix function twice to get both matrixes
matrix1 = fill_matrix(1)
print(matrix1)
matrix2 = fill_matrix(2)
print(matrix2)

# Perform the selected operation
match selected_menu_option:
	case 1: # Addition
		final_matrix = []

		row_index = 0 # Iterate through each row
		while row_index < rows: 
			column_index = 0 # Iterate through each column
			matrix1[row_index]
		
	case 2: # Subtraction
		print("TODO: sub")
	case 3: # Scalar Multiplication
		print("TODO: scalar")
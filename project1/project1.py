
"""
Programming Assignment 1: Matrix Calculator
Author: Geremy Giles
Date: 09/14/2025
Description: A program to perform fundamental matrix operations, including addition, subtraction, and scalar multiplication.
"""

#### Functions ####
def fill_matrix


#### Main Code ####

# Print title
print("Matrix Calculator")
# List menu options
print("1. Addition" + 
	  "\n2. Subtraction" + 
	  "\n3. Scalar Multiplication" + 
	  "\n4. Exit")
# Prompt user input and store in var
menu_option = input("Choose an option listed above: ")
# Validate selection with loop
while menu_option < 0 or menu_option > 4:
	# Print error message and reprompt user
	print("Invalid entry")
	menu_option = input("Choose an option listed above: ")
# Print selected option
print("You selected " + menu_option)
# Prompt user for rows and columns of two matrixes, and store in var
rows_and_columns = input ("Enter the amount of rows and columns in the matrixes, with the following format: “# #”").strip()
# Attempt to splice the input into separate integer variables, and throw and error and reprompt if needed
rows = 0
columns = 0
while rows == 0 and columns == 0:
	try:
		# try to find the index of the space character
		space_index = rows_and_columns.index(" ")
		# Splice the string into rows and colums
		rows = rows_and_columns[0:space_index]
		columns = rows_and_columns[space_index:0]
	except ValueError: 
		# No space found or letters entered, reprompt user
		print("Input error")
		rows_and_columns = input ("Enter the amount of rows and columns in the matrixes, with the following format: “# #”").strip()
# Print a confirmation message and direct to the first matrix
print("Success!" +
	  "\nMatrix 1:" +
	  f"\nEnter the rows of the first {rows}x{columns} matrix:")
matrix1 = []
# start a while loop to iterate until all data has been entered
i = 0
while i < rows: 
	# Prompt the user for the nth row of the matrix
	current_row = input (f"Row {i+1}: ").strip()
	# Verify user input with a loop
	current_row_list = []
	while matrix1.length() < rows:
		try:
			# try to split the input at spaces
			current_row_list =  current_row.split(" ")
			# Check length of list
			if current_row_list.length < columns:
				raise Exception("Incorrect Length")
			else:
				# Check content to ensure they are numbers
				for i in current_row_list:
					if type(i) != int:
						raise ValueError("Non-integer values entered.")
				matrix1.append ( current_row_list )
		except Exception: 
			# User didn’t enter enough data, reprompt
			print("Input error")
			current_row = input("Row {i+1}: ").strip()
		except ValueError: 
			# Input other than integer was received, reprompt user
			print("Input error")
			current_row = input("Row {i+1}: ").strip()

# Print a confirmation message and direct to the second matrix
Print “Success!
Matrix 2:
Enter the rows of the second {rows}x{columns} matrix:”
matrix2 = []
# start a while loop to iterate until all data has been entered
While i < rows: 
# Prompt the user for the nth row of the matrix
String current_row = input ( “Row {i+1}: ” ).strip()
# Verify user input with a loop
current_row_list = []
While matrix2.length() < rows:
Try:
		# try to split the input at spaces
		current_row_list =  current_row.split(“ ”)
		# Check length of list
		if current_row_list.length < columns
			throw(“LengthError”)
		else
			# Check content to ensure they are numbers
			for i in current_row_list
				if type(i) != int
					throw(“ValueError”)
			matrix2.append ( current_row_list )
Except LengthError: 
	# User didn’t enter enough data, reprompt
Print “Input error”
current_row = input ( “Row {i+1}: ” ).strip()
Except ValueError: 
		# Input other than integer was received, reprompt user
		Print “Input error”
current_row = input ( “Row {i+1}: ” ).strip()

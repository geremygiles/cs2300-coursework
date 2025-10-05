"""
Programming Assignment 2: Network/Traffic Flow
Author: Geremy Giles
Date: 10/05/2025
Description: A program that can produce and solve a general solution to a network/traffic flow problem.
"""

#### Imports ####
import numpy as np
import sympy as sp

#### Definitions ####
matrix = None



#### Functions ####


### Main Program ####

# Output the linear equations for the provided network
print("The linear equations for the provided network are:")
print("1) x1 - x2 = 100")
print("2) x3 - x2 = 50")
print("3) x3 - x4 = 120")
print("4) x5 - x4 = 150")
print("5) x5 - x6 = 80")
print("6) x1 - x6 = 100")


# Solve for the general solution with libraries

# Create the augmented matrix
matrix = np.array([[1, -1, 0, 0, 0, 0, 100],
                   [0, -1, 1, 0, 0, 0, 50],
                   [0, 0, 1, -1, 0, 0, 120],
                   [0, 0, 0, -1, 1, 0, 150],
                   [0, 0, 0, 0, 1, -1, 80],
                   [1, 0, 0, 0, 0, -1, 100]])

#matrix = np.array([[1, 1, 0, 0, 625],
#                   [1, 0, 0, 1, 475],
#                   [0, 1, 1, 0, 1050],
#                   [0, 0, 1, 1, 900]])

# Convert to sympy Matrix
sp_matrix = sp.Matrix(matrix)


# Perform row reduction, obtaining the RREF at index 0
rref_matrix = sp_matrix.rref()[0]


# Get pivot columns from index 1
pivot_columns = sp_matrix.rref()[1]


# Display the resulting matrix
print("\nThe RREF of the matrix is:")
sp.pprint(rref_matrix)


# Calculate the free variables
free_variables = []
for i in range(sp_matrix.cols - 1): # Iterate through the columns (excluding the b)
    if i not in pivot_columns: # If the column is listed as a pivot column, add to free variables list
        free_variables.append(i)



# Display the solution (with free variables)
print("\nThe resulting equations are:")
for row in rref_matrix.tolist(): # Get each row
    row_equation = "" # Initialize the row equation
    for item in row: # Get each item in the row
        if item == 1: # If the item is a 1, add the variable to the solution
            row_equation += "x" + str(row.index(item) + 1)
        elif item == -1: # If the item is a -1, subtract the variable from the solution
            row_equation += " - x" + str(row.index(item) + 1)
    if row_equation != "":
        print(row_equation + " = " + str(row[-1])) # Print the row equation

print("\nTherefore, the general solution is:")
for row in rref_matrix.tolist(): # Get each row
    x_variable = "" # Initialize the row equation
    solution = "" # Initialize the solution
    for item in row: # Get each item in the row
        if item == 1: # If the item is a 1, add the variable to the left side
            x_variable += "x" + str(row.index(item) + 1)
        elif item == -1: # If the item is a -1, add the variable to the right side
            solution += "x" + (str(row.index(item) + 1) + " + ")
    if x_variable != "" and solution != "":
        if row[-1] != 0:
            if row[-1] > 0:
                print(x_variable + " = " + solution + str(row[-1])) # Print the row equation
            else:
                solution = solution[:-3] # Remove the last " + " from the solution
                print(x_variable + " = " + solution + " - " + str(abs(row[-1])))
        else:
            solution = solution[:-3] # Remove the last " + " from the solution
            print(x_variable + " = " + solution) # Print the row equation without the 0


# Accept user input for the free variables
user_inputted_vars = {} # Create an empty dictionary to store user inputted variables
for var in free_variables:
    user_inputted_vars[var] = None # Initialize each free variable to None

for var in free_variables:
    while user_inputted_vars[var] == None: # Loop until a valid input is received
        try:
            user_input = input (f"\nEnter the value for x{var + 1}\n").strip() # Prompt for variable value (add 1 for correct variable number)
            user_inputted_vars[var] = int(user_input) # Convert to integer and store in dictionary
        except: 
            # Invalid entry, reprompt user
            print("Invalid entry")

print("\nThe user inputted variables are:")
for var in user_inputted_vars:
    print(f"x{var + 1} = {user_inputted_vars[var]}") # Add 1 to the index to get the correct variable number


# Output the specific solution with the user input

print("\nThe resulting solution is:")
for row in rref_matrix.tolist(): # Get each row
    x_variable = "" # Initialize the row equation
    solution = row[-1] # Initialize the solution to the b value at the end of the row
    for item in row: # Get each item in the row
        if item == 1: # If the item is a 1, add the variable to the solution
            x_variable += "x" + str(row.index(item) + 1)
        elif item == -1: # If the item is a -1, subtract the variable from the solution
            solution += user_inputted_vars[row.index(item)] # Add the user inputted value from the solution value
    if x_variable != "":
        print(x_variable + " = " + str(solution)) # Print the row equation


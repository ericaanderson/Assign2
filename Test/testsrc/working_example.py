# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 07:53:24 2023

@author: erica
"""


#import testmodule.iotest as io
import numpy as np

# =============================================================================
#            This code does not work. Attempt to read the file..
# load_data = io.read_data()
# test_data = []
# for line in load_data:
#     for value in line:
#         row.append(value)
#     test_data.append(row)
# print (test_data)
# =============================================================================

                        # Read and bring in test file # 
  
        # Read and convert Input text file data to integer data type#
test_data = np.loadtxt('C:/Users/erica/OneDrive/Documents/GitHub/Assign2/Test/testsrc/example.txt', dtype=int)
print(test_data)

#print center cell
print(test_data[1][1])

#calculate the length of the collumns and rows
n_row = len(test_data)
n_col = len(test_data[0])

print (n_col)
print (n_row)


def point_coordinates(matrix):
    """
    This function takes the array of test_data as an argument and returns a 
    list of the coordinates of each x and y value in the data
    
    Parameters:
    matrix (list): A list representing the input data
    
    Returns:
    coordinates: A list where the 
    """
 
    coordinates = []       
    # Iterate through the matrix and add the coordinates of each value to the coordinate list
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            point = (x,y)
            coordinates.append(point)     
    return coordinates

print (point_coordinates(test_data))

# establish maximum x and y coordinates as maximum row and column data
max_x = max(point_coordinates(test_data), key=lambda x: x[0])[0]
max_y = max(point_coordinates(test_data), key=lambda y: y[1])[1]

print(max_x)
print(max_y)

        



                    # Neighborhood Boundary Rules #
def boundary_rules(matrix):
    pixel_type = []
    
    # Define x and y    
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            pixel = (x,y)
    
    #Center Cell
            if x != 0 and y != 0:
            	pixel = 'center_cell'
            	neighbor = 8
                
    #North Wall
            elif x == 0 and 1<y<((max_y)-1):
                pixel = 'north'
                neighbor = 5
      
    #South Wall
            elif x == (max_x) and 1<y<((max_y)-1):
            	pixel = 'south'
            	neighbor = 5
    
    #East Wall
            elif 0<x<(max_x -1) and y == (max_y):
            	pixel = 'east'
            	neighbor = 5
            
    #West Wall
            elif 0<x<(max_x -1) and y == 0:
            	pixel = 'west'
            	neighbor = 5
    
    #North West Corner
            elif x == 0 and y == 0:
                pixel = 'northwest'
                neighbor = 3
        
    #South West Corner
            elif x == max_x and y == 0:
            	pixel = 'southwest'
            	neighbor = 3
        
    #North East Corner
            elif x == 0 and y == (max_y):
            	pixel = 'northeast'
            	neighbor = 3
        
    #South East Corner
            elif x == max_x and y == (max_y):
            	pixel = 'southeast'
            	neighbor = 3  
            
            pixel_type.append(pixel)
        return pixel

print (boundary_rules(test_data))
# the above code is only printing out "northeast. struggling to understand why



#the below code was the thoughts behind a calculation for slope. Still working to 
#incorporate the boundary rules. 
# =============================================================================
# def slope(matrix):
#     """
#     This function calculates the slope of the data given two points within the data.
#     
#     Parameters:
#     x1: The x-coordinate of the first point
#     y1: The y-coordinate of the first point
#     x2: The x-coordinate of the second point
#     y2: The y-coordinate of the second point
#     
#     Returns:
#     Number: The slope of the line
#     """
#     # Calculate the rise and run
#     rise = y2 - y1
#     run = x2 - x1
#         
#     # Calculate and return the slope
#     return rise / run
# =============================================================================


                        #Create a GUI
#the below is an initial GUI created but ran into a number of errors during the testing process.
#namely, the asyncrio error. 
# =============================================================================
# def gui():
#     """
#     This function creates a GUI that allows the user to select what file to look at.
#     """
#     # Create the GUI window
#     root = tk.Tk()
#     root.title("DEM Slope Calculator")
#     
#     # Open a file dialog to select output files
#     file_paths = filedialog.askopenfilenames(title="Select Output Files", filetypes=[("Text Files", "*.txt")])
#     
#     # Print the selected file paths
#     for file_path in file_paths:
#         print(file_path)
#         
# print(gui())
# =============================================================================

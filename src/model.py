# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:18:18 2023

@author: erica
"""



import numpy as np
 
  
# Convert text file data converted to integer data type array
input_data = np.loadtxt('C:/Users/erica/OneDrive/Documents/GitHub/Assign2/src/data/input/slope.txt', dtype=int)
print(input_data)


#prints second value in input matrix
print(input_data[0][1])

#prints all data so it's not concacted.
np.set_printoptions(threshold=np.inf)

def calculate_slope(test_data):
    """
    This function calculates the slope in raster data.
    
    Parameters:
    raster_data (numpy.ndarray): A 2D numpy array representing the raster data
    
    Returns:
    numpy.ndarray: A 2D numpy array representing the slope of the raster data
    """
    try:
        # Check if the input is a 2D numpy array
        if not isinstance(input_data, np.ndarray) or len(input_data.shape) != 2:
            raise TypeError("Input must be a 2D numpy array")
        
        # Calculate the slope using the gradient function
        dx, dy = np.gradient(input_data, edge_order=2)
        slope = np.arctan(np.sqrt(dx**2 + dy**2))
        
        return slope
    except TypeError as e:
        # Log the error
        print(f"Error: {e}")
        return None

#create variable to identify slope data from input
slope_data = calculate_slope(input_data)

#print(slope_data)



#finds maximum slope of in column and returns as array (axis 0)
max_slope_columns = np.amax(slope_data, axis = 0)

print (max_slope_columns)
print (len(max_slope_columns))

#finds maximum slope of in row and returns as an array (axis 1)
max_slope_rows = np.amax(slope_data, axis = 1)

print (max_slope_rows)    # print maximum slope in row
print (len(max_slope_rows)) # prints length of row 


#save max slope column and row data into a new file


np.savetxt('C:/Users/erica/OneDrive/Documents/GitHub/Assign2/src/data/output/columnslope.txt', max_slope_columns)            

np.savetxt('C:/Users/erica/OneDrive/Documents/GitHub/Assign2/src/data/output/rowslope.txt', max_slope_rows)



 
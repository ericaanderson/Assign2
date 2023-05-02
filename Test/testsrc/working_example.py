# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 07:53:24 2023

@author: erica
"""


import testmodule.iotest as io
import numpy as np



#print (io.read_data())

 
  
# Text file data converted to integer data type
test_data = np.loadtxt('C:/Users/erica/OneDrive/Documents/GitHub/Assign2/Test/testsrc/testdata/example.txt', dtype=int)
print(test_data)



print(test_data[0][1])

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
        if not isinstance(test_data, np.ndarray) or len(test_data.shape) != 2:
            raise TypeError("Input must be a 2D numpy array")
        
        # Calculate the slope using the gradient function
        dx, dy = np.gradient(test_data, edge_order=2)
        slope = np.arctan(np.sqrt(dx**2 + dy**2))
        
        return slope
    except TypeError as e:
        # Log the error
        print(f"Error: {e}")
        return None

print(calculate_slope(test_data))


 
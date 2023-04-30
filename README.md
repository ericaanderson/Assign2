# Assignment 2 #

About: Assignment 2 
Contact: Erica Anderson
         gy22ea@leeds.ac.uk
Website:
GIT: https://github.com/ericaanderson/Assign2
Security: 
The MIT License (MIT)

Copyright (c) 2015 99designs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contents:

How to:
outline what the software is, how it can be run, and what is to be expected when it is run (how it works.)
This software is designed to calculate the maximum slope values from an input text file populated with raster data. 

To use:
This program works by reading the text file of interest using the NumPy loadtext function and assigning the variable input_data. Data is identified as integers.
A print statement is available to the user is  at any time to identify the values produced in each statement. For example, to 
double check the consistency, the print statement "print(input_data[0][1])" should produce the second value on the matrix. 
The argument np.set_printoptions(threshold = np.inf) aims to allow the user to view all matrix data so it is not concacted. 

The function def calculate_slope(test_data) utilized the raster data that was brought in via loadtext. After ensuring the array is in 2-dimensional format,
np.gradient establishes the difference in positional x and y value (rise and run.) 
"edge_order = 2" Means to calculate the boundary slopes where the typical neighborhood values would be 0, using forward difference and backward difference.
for "slope = np.arctan(np.sqrt(dx**2 + dy**2)" calculates the slope using the established difference. This function returns the slope of the desired data

Calling the function calculate_slope(input_data) calculates the slope of each cell in the matrix and identifies it as the variable slope_data. 

To find the maximum slope of each column within the matrix of input data, "np.amax(slope_data, axis = 0)" is used. np.amax calls axis 0 ( locates the code to the columns.

#finds maximum slope in each column of matrix and returns as array (axis 0)
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



 



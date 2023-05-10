# Assignment 2 #

**About:** Assignment 2   
**Contact:** Erica Anderson  
         gy22ea@leeds.ac.uk    
**GIT:** https://github.com/ericaanderson/Assign2  
**Security:** MIT License  

Copyright (c) 2023 ericaanderson

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

**Contents:**  
Main file contains a 'src' code file where the user will find the program 'model.py' and another file 'data'. 'Model.py' is the program the user will run to retrieve the desired results. The 'data' file, hosts two additional files, 'input' and 'output'. The provided text file is saved in 'input' as "slope" for retrieval within the program 'model.py'. The alternative file 'output' holds the resulting data from the calculations within 'model.py'. There should be two output files available named 'columnslope.txt' and 'rowslope.txt'. 

The main file "Assign2" also contains a 'test' file. This file hosts the research and testing work used to develop the code displayed in model.py. In the end, a third party program NumPy was chosen to create the most efficient and clean code for the user to utilize. 

**How to:**  

This software is designed to calculate the maximum slope values from an input text file populated with raster data and display it to the user through a GUI. 

<u>To use:</u>  
This program works by reading the text file of interest using the NumPy loadtext function and assigning the variable input_data. Data is identified as integers. A print statement is available to the user is  at any time to identify the values produced in each statement. For example, to double check the consistency, the print statement "print(input_data[0][1])" should produce the second value on the matrix. 

The argument np.set_printoptions(threshold = np.inf) aims to allow the user to view all matrix data so it is not concacted. 

The function def calculate_slope(test_data) utilized the raster data that was brought in via loadtext. After ensuring the array is in 2-dimensional format, np.gradient establishes the difference in positional x and y value (rise and run.)  "edge_order = 2" Means to calculate the boundary slopes where the typical neighborhood values would be 0, using forward difference and backward difference. for "slope = np.arctan(np.sqrt(dx**2 + dy**2)" calculates the slope using the established difference. This function returns the slope of the desired data

Calling the function calculate_slope(input_data) calculates the slope of each cell in the matrix and identifies it as the variable slope_data. 

To find the maximum slope of each column within the matrix of the input data, "np.amax(slope_data, axis = 0)" is used. np.amax calls axis 0 to orient code to calculating along the columns. This calculation returns 300 data points representing the maximum slope of that column. This is corroborated by the print statement, "print (len(max_slope_columns))". Similarly, the max_slope_rows calculates the maximum slope found in each row using the familiar call "np.amax(slope_data, axis = 1)". This time, axis = 1 orients the code to checking each row of data along the matrix. 

Following these calculations, the maximum slope of columns and rows are saved into their own new files 'columnslope.txt' and 'rowslope.txt', respectively, using NumPy's savetxt command. 

After running through the GUI and printing any pertinent statements (which can be designated by the user), the program runs a GUI prompt. This allows the user to choose which DEM file to output. Three functions work to establish the framework of the GUI. The ‘upload_raster’ function provides the options of which file to select for reading. The ‘exit_app’ function, when called, will close the prompt. Finally, the ‘gui’ function establishes the framework for the GUI. The main menu is created using the tkinter menu designation. To add actionable items to the menu, add_command is used, labeled, and the previously designated functions ‘ upload_raster’ and ‘exit_app’ are called for each action respectively. 

The output should produce a small message box with the first line of the selected file’s values. The values in these files are the maximum slope of the rows (or columns depending on the file chosen).

 


 



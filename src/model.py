# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:18:18 2023

@author: erica
"""



import numpy as np
import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox

  
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

    # Calculate the slope using the gradient function
    dx, dy = np.gradient(input_data, edge_order=2)
    slope = np.arctan(np.sqrt(dx**2 + dy**2))
        
    return slope


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




    
                #Create a GUI #
def upload_raster():
    """
    This function uploads the saved txt files of maximum slope values depending on which file is selected.

    """
    file_path = filedialog.askopenfilenames (title="Select Output Files", filetypes=[("Text Files", "*.txt")])
    if file_path:
            # have tried several versions of this command without success to get the user to select one file OR the other. 
                #Only have had success with the filepath being outline below. 
            data = np.loadtxt('C:/Users/erica/OneDrive/Documents/GitHub/Assign2/src/data/output/columnslope.txt')
            first_line = data
            messagebox.showinfo("File Selected", f"Selected file: {file_path}\nThe first line of the file is:\n{first_line}")


def exit_app():
    """
    This function closes the GUI

    """
    root.destroy()

def gui():
    """
    This function creates a GUI that allows the user to select what file to look at.
    """
    # Create the GUI window
    global root
    root = tk.Tk()
    root.title("DEM Slope Calculator")
    
    # Create the main menu
    main_menu = tk.Menu(root)
    
    # Open a file dialog to select output files
    file_menu = tk.Menu(main_menu, tearoff=0)
    file_menu.add_command(label="Upload Raster of choice", command=upload_raster)
    file_menu.add_command(label="Exit", command=exit_app)
    
      
    # Add the "File" submenu to the main menu
    main_menu.add_cascade(label="File", menu=file_menu)

    # Configure the root window to display the menu
    root.config(menu=main_menu)

    root.mainloop()
      

if __name__ == "__main__":
    gui()




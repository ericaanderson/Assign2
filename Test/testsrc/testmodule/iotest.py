# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 07:45:21 2023

@author: erica
"""

import csv

def read_data():
    '''
    Reads input data file

    Returns
    -------
    data : numbers

    '''
    with open ('C:/Users/erica/OneDrive/Documents/GitHub/Assign2/Test/testsrc/example.txt', "r") as f:
        data = f.read()
    return (data)

print(read_data())
    
# =============================================================================
# 	f = open ('C:/Users/erica/OneDrive/Documents/GitHub/Assign2/Test/testsrc/testdata/input/example.txt', newline='')
# 	data = [ ]
# 	for line in csv.reader(f, quoting = csv.QUOTE_NONNUMERIC):
# 		row = [ ]
# 		for value in line:
# 			row.append(value)
# 		data.append(row)
# 	f.close()
# 	n_rows = len(data)
# 	n_cols = len(data[0])
# 	return (data, n_rows, n_cols)
# =============================================================================



def write_data(self):
    '''
    Write maximum slope data to a file

    Returns
    ---
    None
    '''
    file = 'C:/Users/erica/OneDrive/Documents/GitHub/Assign2/Test/testsrc/testdata/output.txt'
    with open(file, 'wb') as output_file:
        output_file.write(self)
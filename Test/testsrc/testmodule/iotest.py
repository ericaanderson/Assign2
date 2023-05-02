# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 07:45:21 2023

@author: erica
"""

import csv

def read_data():
	'''
    Opens file and reads data. Appends material in csv to an iterable list that will be readable by the rest of the code.

    Returns
    —-
    Number
    '''
	f = open ('C:/Users/erica/OneDrive/Documents/GitHub/Assign2/Test/testsrc/testdata/example.txt', newline = '')
	data = [ ]
	for line in csv.reader( f, quoting = csv.QUOTE_NONNUMERIC):
		row = [ ]
		for value in line:
			row.append(value)
		data.append(row)
	f.close()
	n_rows = len(data)
	n_cols = len(data[0])
	return (data, n_rows, n_cols)
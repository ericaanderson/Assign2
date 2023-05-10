# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:24:21 2023

@author: erica
"""

                    # Neighborhood Boundary Rules #

#Center Cell
if x != 0 and y != 0:
	pixel = 'center_cell'
	neighbor = 8

#North Wall
if x = 0 and 1<y<(max(n_col) -1):
	pixel = 'north'
	neighbor = 5
  
#South Wall
if x = (max(n_row)) and 1<y<(max(n_col) -1):
	pixel = 'south'
	neighbor = 5

#East Wall
 if x = 0<x<(max(n_row) -1) and y = (max(n_col))
	pixel = 'east'
		neighbor = 5
        
#West Wall
if 0<x<(max(n_row) -1) and y = 0
		pixel = 'west'
		neighbor = 5

#North West Corner
if n_row = 0 and n_col = 0:
    pixel = 'northwest'
	neighbor = 3
    
#South West Corner
if n_row = max(n_row) and n_col = 0
	pixel = 'southwest'
	neighbor = 3
    
#North East Corner
if n_row = 0 , and n_col = max(n_col)
	pixel = 'northeast'
	neighbor = 3
    
#South East Corner
if n_row = max(n_row) and n_col = max(n_col)
	pixel = 'southeast'
	neighbor = 3
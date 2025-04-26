#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:11:02 2021

@author: liangyitian
"""

import csv
VD = "Vaccine_Distribution.csv"

        
def read_csv(filename):
    ''' Function: read_csv
        Parameters: filename, a string
        Returns: 2d list of strings, the contents of the file
    '''
    data = []
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ",")
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data

def get_col(table, col, cast = str):
    ''' Function: get_col
        Parameters: table, a 2d list of anything, and col an int
        Returns: all the data for that column, as a list
    '''
    col_data = []
    for row in table:
        col_data.append(cast(row[col]))
    return col_data

if __name__ == "__main__":
    
    a = read_csv(VD)
    print(a)
    
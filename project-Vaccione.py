#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 09:00:22 2021

@author: 
    xiechuman, liangyitian, chenyongru
"""
"""
DS2001 Final Project
Team Members: Chuman Xie, Yitian Liang, Yongru Chen
Statement: Which state has the most vaccines distributed comparing with other states?
Visualization: Bar chart + Map

"""


import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

MODERNA = "COVID-19_Vaccine_Distribution_Allocations_by_Jurisdiction_-_Moderna.csv"


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


def vaccine_by_state(states, vaccines):
    ''' Function: vaccine_by_state
        Parameters: list of state(strings),
                    list of vaccines (ints), same length
        Return: dictionary where key = state (string),
                value is a list of vaccine numbers (ints)
                ex: {"Connecticut" : [37400, 37400, 35800, ...]}
    '''
    state_dict = {}
    for i in range(len(states)):
        if states[i] in state_dict:
            state_dict[states[i]].append(vaccines[i])
        else:
            state_dict[states[i]] = [vaccines[i]]
    return state_dict
        

def count_categories(dictionary):
    ''' Function: count_categories
        Parameters: a dictionary
        Returns: total number of values for each category
    '''

    dic = {}
    for k, v in dictionary.items():
        sum = 0
        for i in range(len(dictionary[k])):
            sum += dictionary[k][i]
            dic[k] = sum
    return dic 


def max_vaccines(dictionary):
    ''' Function: max_vaccines
        Parameters: a dictionary
        Returns: a tuple containing a string and int,
                 the biggiest number of vaccines among states and its count
    '''
    max_count = -1
    max_vaccine = ""
    for key, value in dictionary.items():
        if value > max_count:
            max_count = value
            max_vaccine = key
    return (max_vaccine, max_count)

# def draw_from_dict(dicdata,RANGE):
#     by_value = sorted(dicdata.items(),key = lambda item:item[1],reverse=True)
#     x = []
#     y = []
#     for d in by_value:
#         x.append(d[0])
#         y.append(d[1])
#         plt.barh(x[0:RANGE], y[0:RANGE])
#         plt.ylabel('states')
#         plt.xlabel('number of vaccine')
#         plt.legend()
#         plt.show()
#     return
        
  
if __name__ == "__main__":
    # get the data and pull out the first dose colum, and the state column,
    # each into their own lists
    
    vaccines = read_csv(MODERNA)
    first_dose = get_col(vaccines, 2, cast = int)
    states = get_col(vaccines, 0, cast = str)
    
    # call out vaccine_by_state function to get the number of vaccines for each state
    # since the number of 1st dose is the same as 2nd dose,
    # we will only calculate 1st dose here. 
    
    state_dict = vaccine_by_state(states, first_dose)
    print(state_dict)
    
    first_dose_sum = count_categories(state_dict)
    
    # call out max_vaccines function to get which state has the most vaccines
    max_state = max_vaccines(first_dose_sum)
    
    print(first_dose_sum)
    print()
    print("This state has the most vaccines distribution:", max_state)
  
    # use Panda to get a visualized date view
    # df = pd.DataFrame(state_dict)
    # df.value_counts()
    # print(df)
    
    # draw_from_dict(first_dose_sum, 56)
    
    plt.bar(range(len(first_dose_sum)),list(first_dose_sum.values()),
            align = "center")
    plt.xticks(range(len(first_dose_sum)), list(first_dose_sum.keys()))
    plt.xticks(size='small',rotation=90,fontsize=5)
    plt.ylabel('states')
    plt.xlabel('number of vaccine')
    plt.show()
    
    plt.figure(2)
    
    blist=[]
    clist=[]
    list=sorted(first_dose_sum.items(),key=lambda item:item[1], 
                reverse = True)
    for i in list:

        blist.append(i[0])
        clist.append(i[1])
    plt.bar(range(len(blist)), clist, tick_label=blist)
    plt.xticks(size='small',rotation=90,fontsize=5)
    plt.ylabel('states')
    plt.xlabel('number of vaccine')
    plt.show()
    
    
    plt.figure(3)
    
    print(clist)
    tt = clist[0,10]
    print(tt)
    
    # vac = 0
    # dlist = []
    # for i in clist(0,9):
    #     dlist.append(i)
    # for i in clist(10,-1):
    #     vac += i
    # dlist.append(vac)
    # print(dlist)
            
                
        
    
    plt.figure(figsize=(8,8))
    plt.pie(clist,labels=blist,autopct='%1.1f%%')
    plt.title('number of vaccine')
    plt.show()

    
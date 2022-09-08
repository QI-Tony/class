
# file: hw2.py
# author: Qi Zhang
#  implement 6 function


import csv
import numpy as np
import sqlite3


#  to check the if input integer is the power of 2 
#  inti: input integer
def is_power_of_2(inti):
    if inti== 0:
        return False
    if inti == 1:
        return True
    if (inti%2 == 0):
        return is_power_of_2(inti/2)
    else:
        return False
    

#     to check if the integer in a 2d list is power of 2
#     martix: the nparray.
def all_power_of_2(martix = np.array([[]])):
    for i in martix.flat:
        if not is_power_of_2(i):
           return False
    return True



#  to report the coordinate of the number 
def first_divisible(arr,d=2):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] %d == 0:
                return[i,j]
#  This function takes a nonempty numpy matrix and returns a list of all elements
# that have indices that sum to a multiple of 4.
def multiples_of_4(array):
    ret = []
    new = array.shape
    for i in range(new[0]):
        for j in range(new[1]):
            if((i+j) % 4 == 0):
                ret.append(array[i,j])
    return ret
# n takes a dictionary that maps keys to lists of numbers and returns a numpy
# matrix containing the numbers in the lists
def to_array(dic):
    ret=[]
    for key in dic:
        ret.append(dic[key])
    return np.array(ret)
    
    
# adds a new table with the specified name to 
# the db that has the information from the csv
# file in it
def to_table(csvfile,sqlfile,tablename="New1"):
    sever = sqlite3.connect(sqlfile)
    with open(csvfile) as f:
        reader = csv.reader(f)
        headers = tuple(next(reader))
        cur = sever.cursor()
        cur.execute("CREATE TABLE {} {};".format(tablename,headers))
        for i in reader:
            cur.execute("INSERT INTO {} {} VALUES {}; ".format(tablename,headers,tuple(i)))
    sever.commit()
    sever.close()




import unittest, numpy as np, pandas as pd, json, sqlite3 
import inspect
import datetime

# file: hw3.py
# author: Qi Zhang
# Class: ista131
#  implement 5 function by using pandas and More SQL

# This function takes a connection object, and two string and one integer
# to print the required information from database
def A_students (conn, table_name = "ISTA_131_F17", st_str = None, num_results = 10):
    cursor = conn. cursor()
    if st_str == None:
        cursor.execute("SELECT LAST, FIRST FROM "+table_name+" WHERE GRADE = 'A' order by LAST ASC")
    else:
        st_str = st_str.capitalize()
        cursor.execute("SELECT LAST, FIRST FROM "+table_name+" WHERE GRADE = 'A' AND LEVEL = '" +st_str+"'order by LAST ASC")
    ret = []
    for i in cursor.fetchall()[:num_results]:
        strs = str(i[0])+", "+str(i[1])
        ret.append(strs)
    return ret
# this function to Read a csv file and return a DataFrame
def read_frame():
   col_names = ['Jan_r', 'Jan_s', 'Feb_r', 'Feb_s', 'Mar_r', 'Mar_s', 'Apr_r','Apr_s', 'May_r', 'May_s', 'Jun_r', 'Jun_s', 'Jul_r', 'Jul_s', 'Aug_r',
'Aug_s', 'Sep_r', 'Sep_s', 'Oct_r', 'Oct_s', 'Nov_r', 'Nov_s', 'Dec_r','Dec_s']
   frame = pd.read_csv('sunrise_sunset.csv', header = None, names = col_names, index_col = 0, dtype ='str')
   return frame


# takes a sun DataFrame as created by the previous function and returns
# two Series,
def get_series(sun_frame):
#     set mounth
    mounth = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#     sun set and sun rise
    sun_rise = pd.concat([sun_frame[m + '_r'] for m in mounth])
    sun_set = pd.concat([sun_frame[m + '_s'] for m in mounth])
    sun_rise.dropna(inplace = True)
    sun_set.dropna(inplace = True)
    date = pd.date_range('010118','123118')
#     set index
    sun_set.index = date
    sun_rise.index = date
    return sun_rise, sun_set

# This function takes sunrise and sunset Series and returns the timestamp of the
# longest day and an hour-minute string that represents the length of that day
# (just like the strings in the Series
def longest_day(sun_rise,sun_set):
    rise_new = sun_rise.astype(int)
    set_new = sun_set.astype(int)
#     get the value set mines rise
    ranges = set_new - rise_new
    return(ranges.idxmax(),str(ranges[ranges.idxmax()]))
# This function takes a sunrise Series and a timestamp. It returns the difference in
# minutes between the sunrise time 90 days before the timestamp and 90 days after
def sunrise_dif(rise,tamp):
    rise_new = ((rise.astype(int)// 100) * 60) + (rise.astype(int) % 100)
    a = tamp - datetime.timedelta(90)
    b = tamp + datetime.timedelta(90)
    ret = rise_new.loc[a] - rise_new.loc[b]
    return ret

    
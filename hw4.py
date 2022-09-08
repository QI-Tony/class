import unittest, sys, pandas as pd, sqlite3
import numpy as np

# file: hw4.py
# author: Qi Zhang
# Class: ista131
#  implement 8 function by using pandas and More SQL. Pricticeing the cvs frame



# This function takes a csv filename as an argument 
# and cheng"," to "."
def csv_to_dataframe(csvname):
    df = pd.read_csv(csvname,index_col = 0,decimal = ',')  
    return df


# his function takes a countries DataFrame as created by the previous function

def format_df(df):
    df['Region'] = df['Region'].str.title().str.strip()
    df.index = df.index.str.strip()
    # inplace = ture mean change the df, not create a duplication
    df.set_index(df.index.values, inplace = True)
    
# It adds a new column labeled 'Growth Rate'totheframe
def growth_rate(df):
    df['Growth Rate'] = df['Birthrate'] - df['Deathrate']


def dod(p, r):
    num_yrs = 0
    while p > 2:
        p = p + p * r / 1000
        num_yrs += 1
    return num_yrs  

# This function takes a formatted countries DataFrame that has a 
# Growth Rate column and adds a column labeled 'Years to Extinction'
def years_to_extinction(df):
    df['Years to Extinction'] =  np.nan
    for i in df.index:
        x = df.index.get_loc(i)
        if df.iloc[x,-2] < 0:
            df.iloc[x,-1] = dod(df.iloc[x,1], df.iloc[x,-2])
        
# This function takes a formatted countries DataFrame that has a Years to Extinction 
# column and returns a Series whose labels are the countries with negative growth rates
def dying_countries(df):
    # Remove missing values.
    return df['Years to Extinction'].dropna().sort_values()


# his function takes a connection object and two table names and returns a sorted list of
# the last names of the students that did better in the class represented by the second table than they did
# in the first. 
def improved(conn, tablea, tableb):
    cursor = conn. cursor()
    cursor.execute("SELECT "+tablea+".LAST, "+tablea+".grade FROM "+tablea
                   +" INNER JOIN "+tableb+" ON "+tablea+".LAST = "+tableb+".LAST AND "
                   +tablea+".GRADE < "+tableb+".GRADE")
    ret = []
    for i in cursor.fetchall():
        ret.append(i[0])
    return sorted(ret)

# main creates a frame from countries_of_the_world.csv, formats the frame, adds Growth Rate 
# and Years to Extinction columns to it, and prints the top 5 dying countries in this format
def main():
    df = csv_to_dataframe('countries_of_the_world.csv')
    format_df(df)
    growth_rate(df)
    years_to_extinction(df)
    y = df['Years to Extinction'].dropna().sort_values().head(5)
    for i in y.index:
        print(str(i) + ': ' + str(y[i]) + " Years to Extinction")





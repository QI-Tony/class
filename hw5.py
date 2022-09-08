
import unittest, json, pandas as pd, os, numpy as np, inspect
from compare_pandas import *
import datetime
# file: hw5.py
# author: Qi Zhang
# Class: ista131
#  to load the data into pandas, clean it, reformat it and
#  write two new files to disk covering 1979-2021 and 2022, respectively, in csv format.
#  and implenment the neccessary functions

# Use the data in N_seaice_extent_daily_v3.0.csv to create and returna Series object.
def get_data():
    # read file
    df = pd.read_csv("N_seaice_extent_daily_v3.0.csv", skiprows=2,names=[0, 1, 2, 'Extent'], 
                     usecols=[0, 1, 2, 3], parse_dates={'Dates':[0, 1, 2]}, header=None)
    
    df.index = df["Dates"]
    df_extent = df["Extent"]
    # got all data index from 1978,10,26 to 2022,2,13
    start = datetime.datetime(1978, 10, 26)
    end = datetime.datetime(2022, 2, 13)
    index = pd.date_range(start, end)
    # reindex it
    df_extent.reindex(index)
    return df_extent.reindex(index)

# This function takes the Series created in get_data and alters it in place by 
# filling in the missing data
def clean_data(Series):
    # set 2/20/2021 and 2/21/2021
    Series.iloc[15458] = (Series.iloc[15457]+Series.iloc[15460])/2
    Series.iloc[15459] = (Series.iloc[15457]+Series.iloc[15460])/2
    # set by day
    for i in range(len(Series.index)):
        if str(Series.iloc[i]) == "nan"and str(Series.iloc[i-1]) != "nan"and str(Series.iloc[i+1])!="nan":
            average = (Series.iloc[i-1] + Series.iloc[i+1])/2
            Series.iloc[i] = average
    # set by year
    for j in range(len(Series.index)):
        if(str(Series.iloc[j]) == "nan"):
            j_b = Series.index[j-365]
            j_a = Series.index[j+366]                    
            Series.iloc[j] = (Series[j_b] + Series[j_a]) / 2

#  Generate and return a list of strings that will be used as column labels in a DataFrame
def get_column_labels():
    mmdd = []
    start = datetime.datetime(2021, 1, 1)
    end = datetime.datetime(2021, 12,31)
    index = pd.date_range(start, end)
    for i in index:
        # padding with 0
        if len(str(i.day)) == 1:
            day = "0"+str(i.day)
        else:
            day = str(i.day)
            # padding with 0
        if len(str(i.month)) == 1:
            month = "0"+str(i.month)
        else:
            month = str(i.month)
        mmdd.append(month+day) 
    return mmdd
#This function takes the cleaned Series as its 
# argument and creates and returns a new DataFrame
def extract_df(data):
    # set index
    lables = [year for year in range(1979, 2022)]
    mmdd = get_column_labels()
    matrix = []
    for i in lables:
        row = []
        # to find the value in a datetime
        for index in data.index:
            if str(i) == str(index.year) and (str(index.month)+str(index.day) !="229" ):
                row.append(data.loc[index])
        matrix.append(row)

    frame = pd.DataFrame(matrix,lables, mmdd,dtype=np.float64)
    return frame
# This function takes the cleaned Seriesas its argument and returns a Series
# containing the data for 2022.  
def extract_2022(data):
    for i in range(len(data.index)):
        if(data.index[i].year == 2022):
            index_2022 = i
            return data.iloc[index_2022:]

# Use the above functions to read in the data we want, 
# clean it, and store it to disk in the files data_79_21.csv and data_2022.csv using the to_csv methods for frames and Series.
def main():
    Series = get_data()
    clean_data(Series)
    extract_df(Series).to_csv("data_79_21.csv")
    extract_2022(Series).to_csv("data_2022.csv",header=False)
import unittest, inspect
from compare_pandas import *
import pandas as pd
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
# Author: Qi Zhang
# implement three function which analyze the dataframe
# then draw a graph by using matplotlit


# This function reads the lists from data_2022.csv, and returns a Series
def get_2022():
    lists = []
    mmdd = pd.date_range(start='01/01/2022', end='02/13/2022').strftime('%m%d').tolist()
    df = pd.read_csv("data_2022.csv", header=None)

    for x in range(len(df)):
        lists.append(df.iloc[x,1])
    return pd.Series(lists, mmdd)



# This function takes the DataFrame
# Use the std method passing in the keyword argument ddof=1.
def extract_fig_1_frame(df):
    lists = [[], []]
    for i in range(len(df.columns)):
        lists[0].append(round(df.iloc[:,i].mean(), 6))
        lists[1].append(round(df.iloc[:,i].std() * 2, 6))
    index = ["mean", "two_s"]
    new_df = pd.DataFrame(lists, index, df.columns)
    return new_df


# This function takes the DataFrame
# returns a frame which are the decadal means for the given day of the year

def extract_fig_2_frame(df):
    index = ["1980s", "1990s", "2000s", "2010s"]
    lists = [[], [], [], []]
    for i in range(len(df.columns)):
        lists[0].append(round(df.iloc[1:11,i].mean(), 4))
        lists[1].append(round(df.iloc[11:21,i].mean(), 4))
        lists[2].append(round(df.iloc[21:31,i].mean(), 4))
        lists[3].append(round(df.iloc[31:41,i].mean(), 4))
    new_df = pd.DataFrame(lists, index, df.columns)
    return new_df


# This function takes a figure 1 frame an/d a hw5 frame, and creates a figure 
def make_fig_1(f1, df):
    f1.loc["mean"].plot()
    ax = plt.gca()

    ax.set_ylabel("NH Sea Ice Extent ($10^6$ km$^2$)")
    ax.yaxis.label.set_fontsize(10)
    
    df.loc[2012].plot(linestyle="--")
    xs = np.arange(365)
    yuppers = (f1.loc["mean"]+f1.loc["two_s"]).values.astype(float)
    ylowers = (f1.loc["mean"]-f1.loc["two_s"]).values.astype(float)
    ax.fill_between(xs, yuppers, ylowers, color = "lightgray", label = "$\pm$ 2 std")
    ax.legend()
    

# This function takes a figure 2 frame and creates a figure
def make_fig_2(f2, df):
    ax = plt.gca()    
    ax.set_ylabel("NH Sea Ice Extent ($10^6$ km$^2$)")
    ax.yaxis.label.set_fontsize(10)
    f2.loc["1980s"].plot(linestyle="--")
    f2.loc["1990s"].plot(linestyle="--")
    f2.loc["2000s"].plot(linestyle="--")
    f2.loc["2010s"].plot(linestyle="--")
    ts = get_2022()
    ts.plot(linestyle="-", label = "2022")
    ax.set_xticklabels(["1","0101", "0220", "0411", "0531", "0720", "0908", "1028", "1217","1"])
    ax.legend()
#  main function
def main():
    df = pd.read_csv("data_79_21.csv", index_col = 0)
    f1 = extract_fig_1_frame(df)
    make_fig_1(f1, df)
    plt.figure()
    f2 = extract_fig_2_frame(df)
    make_fig_2(f2, df)
    plt.show()


main()
import csv 
import pandas as pd
import statistics as stat
import numpy as np

def similarValue(dframe):
    colList = []
    for j in range(0,287):
        # Get modus value from j column
        topEl = stat.mode(dframe.iloc[:,j])
        duplicate = 0
        # Loop comparing each row with modus
        for i in range(0,74):
            comp = dframe.iloc[i,j]
            if comp == topEl:
                duplicate += 1
        if duplicate >= 37 :
            colList.append(j)    
    return colList

def simvalTwo(dframe):
    colList = []
    for j in range(1,287):
        # Get modus value from j column
        topEl = stat.mode(dframe.iloc[:,j])
        print(topEl)
        #c Counted modus from list
        # columned = dframe.
        listed = dframe.iloc[:,j]
        counted = listed.count(topEl)
        if counted >= 37 :
            colList.append(j)    
    return colList


dtCdk = pd.read_csv("data/cdk_desc.csv", delimiter=' ')

svOne = similarValue(dtCdk)
svTwo = simvalTwo(dtCdk)

# print(dtCdk)
print(svOne)
print(svTwo)
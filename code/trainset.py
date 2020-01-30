import csv 
import pandas as pd
import statistics as stat
import numpy as np

#STEP 1 : COUNT ALL SIMILARITIES IN 1 ROW
#STEP 2 : IF COUNTED SIMILARITIES MORE THAN 37, DELETE COLUMN

pd.set_option('display.max_row', 3778)
pd.set_option('display.max_column', 3778)

dtTrain = pd.read_csv("data/TrainSetNoId.csv")
dtTrainRaw = dtTrain
dtCdk = pd.read_csv("data/cdk_desc.csv", delimiter=' ')

def similarValue(dframe):
    colList = []
    for j in range(0,3775):
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

def stdDeviation(dframe):
    stdevList = []
    # sample = dframe.iloc[:,1]
    sample = dframe.columns.values
    # sample = dframe.loc['ATSv6']
    print(sample)
    # for j in range(0,len(dframe)):
    #     # Loop search standard deviation each column
    #     stddev = 0
    #     sample = dframe.iloc[:,j]
    #     print(sample)
    #     stddev = stat.stdev(sample)
    #     print(dframe.columns[j], stddev)
    #     if stddev <= 0.95 :
    #         stdevList.append(j)
    return stdevList

def dropColumn(dframe, tList):
    dropped = pd.DataFrame()
    dropped = dframe.drop(dframe.columns[tList], axis=1)
    return dropped


#Create Duplicate List
dupList = []

##### STEP 1 Reduces similarity
simValList = similarValue(dtTrain)
dtSimVal = dropColumn(dtTrain,simValList)
print("================ REDUCED: SIMILARITY VALUES (", len(simValList)," Columns) =================")
print(dtSimVal)

##### STEP 2 Reduce columns by Standard Deviation



sdList = stdDeviation(dtSimVal)
print(len(dtSimVal.columns))
# print(dtTrainRaw.iloc[:,1])
# print(sdList)

# print(max(dtSimVal.iloc[:,2]))
# print(dtTrain.columns.values[simValList[688]])
# print(dtSimVal)
# print(dupList)

# simDF = dropColumn(similarValue,dupList)
# dropColumn(similarValue)
# getIndexTitle(dupList)
# print(simDF)
# print("Duplicate : " , dupList)


# # print(dtTrain[0].name)
# print(dt.iloc[0].Ts) # iloc : Gets row on index 0
# print(dtTrain.iloc[0].AMR)
# # print(dt.Name.head())
# # print("Padel : " , dt.iloc[1].ALogP) #gets all on row 

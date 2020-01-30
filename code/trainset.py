import csv 
import pandas as pd
import statistics as stat
import numpy as np

#STEP 1 : COUNT ALL SIMILARITIES IN 1 ROW
#STEP 2 : IF COUNTED SIMILARITIES MORE THAN 37, DELETE COLUMN

pd.set_option('display.max_row', 100)
# pd.set_option('display.max_column', 3778)

dtTrain = pd.read_csv("data/TrainSetNoId.csv")
dtCdk = pd.read_csv("data/cdk_desc.csv", delimiter=' ')

def similarValue(dframe):
    duplist = []
    for j in range(0,3775):
        # Get modus value from j column
        topEl = stat.mode(dframe.iloc[:,j])
        # print("Modus :  ", topEl)
        duplicate = 0
        # Loop comparing each row with modus
        for i in range(0,74):
            # print(i, dtTrain.iloc[i,j])
            comp = dframe.iloc[i,j]
            if comp == topEl:
                duplicate += 1
        # print(duplicate)
        if duplicate >= 37 :
            duplist.append(j)    
    return duplist

def dropColumn(dframe, tList):
    dropped = pd.DataFrame()
    # for i in range(0,len(tList)):
    #     dropMe = dframe.columns.values[tList[i]]
    #     del dframe[(dropMe)]
    dropped = dframe.drop(dframe.columns[tList], axis=1)
    # dropped = dframe
    # print(dropped)
    return dropped

#print all values on index 0
# print(dtTrain.iloc[0])

# print all row on index 0
# print(max(dtTrain.iloc[:,0]))
# print (dtTrain.iloc[0,0])

# for key,value in dtTrain.iteritems():
#    print (key,value)

#Loop through Title Column(Head)
dupList = []

### STEP 1 Similarities by === (EQUAL)
# print(dtTrain.iloc[:,0:3])
simValList = similarValue(dtTrain)
# print(type(simValList))
dtSimVal = dropColumn(dtTrain,simValList)

# print(simValList[0])
print(type(simValList))
print(dtTrain)
print("=================================")
print(dtSimVal)
# print(simValList)
# print(dtTrain.columns.values[simValList[1]])
print(len(simValList))

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

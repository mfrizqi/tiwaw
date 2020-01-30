import csv 
import pandas as pd
from collections import Counter
import numpy as np

#STEP 1 : COUNT ALL SIMILARITIES IN 1 ROW
#STEP 2 : IF COUNTED SIMILARITIES MORE THAN 37, DELETE COLUMN

# pd.set_option('display.max_row', 100)
pd.set_option('display.max_column', 3778)

dtTrain = pd.read_csv("data/TrainSetNoId.csv")
dtCdk = pd.read_csv("data/cdk_desc.csv", delimiter=' ')

def similarValue(dataframe):
    for j in range(0,3775):
        # Get modus value from j column
        topEl = max(dtTrain.iloc[:,j])
        # print("Modus :  ", topEl)
        duplicate = 0
        # Loop comparing each row with modus
        for i in range(0,74):
            # print(i, dtTrain.iloc[i,j])
            comp = dtTrain.iloc[i,j]
            if comp == topEl:
                duplicate += 1
        # print(duplicate)
        dupList.append(duplicate)

def getIndexTitle(list):
    print(list)

### STEP 1.1 Similarities by === (EQUAL)

#print all values on index 0
# print(dtTrain.iloc[0])

# print all row on index 0
# print(max(dtTrain.iloc[:,0]))
# print (dtTrain.iloc[0,0])

# for key,value in dtTrain.iteritems():
#    print (key,value)

#Loop through Title Column(Head)
dupList = []
similarValue(dtTrain)
getIndexTitle(dupList)
# print("Duplicate : " , dupList)


# # print(dtTrain[0].name)
# print(dt.iloc[0].Ts) # iloc : Gets row on index 0
# print(dtTrain.iloc[0].AMR)
# # print(dt.Name.head())
# # print("Padel : " , dt.iloc[1].ALogP) #gets all on row 

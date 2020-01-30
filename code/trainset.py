import csv 
import pandas as pd
import numpy as np

#STEP 1 : COUNT ALL SIMILARITIES IN 1 ROW
#STEP 2 : IF COUNTED SIMILARITIES MORE THAN 37, DELETE COLUMN

# pd.set_option('display.max_row', 100)
pd.set_option('display.max_column', 3778)

dtTrain = pd.read_csv("data/TrainSetNoId.csv")
dtCdk = pd.read_csv("data/cdk_desc.csv", delimiter=' ')

# def simValueInt(dataframe):
#     for header in range(0,3777):

#         print("")


### STEP 1.1 Similarities by === (EQUAL)

#print all values on index 0
print(type(dtTrain.iloc[0]))
print(type(dtCdk.columns.values[10]))

# print all row on index 0
# print(dtTrain.iloc[:,0])

# # print (dtTrain)
# # print(dtTrain[0].name)
# print(dt.iloc[0].Ts) # iloc : Gets row on index 0
# print(dtTrain.iloc[0].AMR)
# # print(dt.Name.head())
# # print("Padel : " , dt.iloc[1].ALogP) #gets all on row 

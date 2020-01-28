import csv 
import pandas as pd
import numpy as np

#STEP 1 : COUNT ALL SIMILARITIES IN 1 ROW
#STEP 2 : IF COUNTED SIMILARITIES MORE THAN 37, DELETE COLUMN

# pd.set_option('display.max_row', 100)
pd.set_option('display.max_column', 3778)

dtTrain = pd.read_csv("TrainSet.csv")
dt = pd.read_csv("padel_desc.csv")

# def simValueInt(dataframe):
#     for header in range(0,3777):

#         print("")


### STEP 1.1 Similarities by === (EQUAL)

# print (dtTrain)
print(dtTrain[0].name)
# print("Mordred : " , dtMor.iloc[1].name) #gets all on row 

import csv 
import pandas as pd
import numpy as np

#STEP 1 : COUNT ALL SIMILARITIES IN 1 ROW
#STEP 2 : IF COUNTED SIMILARITIES MORE THAN 37, DELETE COLUMN

# pd.set_option('display.max_row', 100)
pd.set_option('display.max_column', 3778)

dtTrain = pd.read_csv("TrainSet.csv")
# dtHeadCdk = dtCdk.columns.values #get all CDK columns name

dt = pd.read_csv("padel_desc.csv")
# dtHeadCdk = dtCdk.columns.values #get all CDK columns name


# print (dtTrain)
print(dt)

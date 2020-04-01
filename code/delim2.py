import csv 
import pandas as pd
import numpy as np

# with pandas
dtCdk = pd.read_csv("data/cdk_desc.csv", delimiter=' ')
dtColCdk = dtCdk.columns.values #get all CDK columns name

dtMor = pd.read_csv("data/mordred_desc.csv")
dtColMor = dtMor.columns.values #get all CDK columns name

dtPadel = pd.read_csv("data/padel_desc.csv")
dtColPad = dtPadel.columns.values #get all CDK columns name

dtRawIC50 = pd.read_csv("data/pIC50_target.csv")
dtIC50 = dtRawIC50['pIC50']

def last(self,n):
    return self.iloc[:,-n:]

# #Get data from csv
# print(" ")
# print("CDK index 1 title: " , dtCdk.iloc[1].Title) #gets data nrow on column series
# # print("")
# print(dtHeadCdk[286]) #Get single CDK column name
# # print("")
# print(dtHeadMor[1561]) #Get single CDK column name
# # print("")
# print(dtHeadPad[1875]) #Get single CDK column name
# print("")
# # funcOne(10)

# === Concate all dataframe (Mordred,Padel,Cdk,Target) ===

# 0. Get all header name for put to front of Dataframe
cdkFirst = dtCdk.loc[:,(dtColCdk[0])] #Get Title
morFirst = dtMor.loc[:,(dtColMor[0])] #Get name
padFirst = dtPadel.loc[:,(dtColPad[0])] #Get Name
 
mixFirst = pd.concat([cdkFirst,padFirst,morFirst], axis = 1)
mixData= pd.concat([dtMor, dtPadel, dtCdk, dtIC50], axis=1)

#Deleting id from concat data

del mixData[(dtColCdk[0])]
del mixData[(dtColMor[0])]
del mixData[(dtColPad[0])]

# Concate Identity to rawData
# completeData = pd.concat([mixFirst,mixData], axis = 1)
# cd = completeData

# 1. SPLITTING INTO TRAIN & TEST DATA
#split 4:1 mixed dataframe random (4 Train : 1 Test)
#ratio train = 0.8

# GET TRAIN SET USING FRAC 0.8 RATIO using frac syntax

TrainSet = mixData.sample(frac=0.8, random_state=45)
# print(TrainSet)
idxList = ( list(TrainSet.index.values))
# print(len(idxList))
# print(type(idxList))

# print (TrainSet)

# print (TestSet)

print(mixData)

# GET TEST SET BY DROP ROWS BASED TRAINSET ROWS
TestSet = mixData.drop(idxList)

#CHECK BOTH DATAFRAME
print("----- TRAIN SET -----")
print(TrainSet)
print("")
print("")
print("")
print("----- TRAIN SET -----")
print(TestSet)

#EXPORT TRAIN&TEST SET TO CSV

# TrainSet.to_csv (r'D:\Code\python\pandas\Exercise\TrainSetNoId.csv',index=False, header=True, sep=',') #Don't forget to add '.csv' at the end of the path
# TestSet.to_csv (r'D:\Code\python\pandas\Exercise\TestSetNoId.csv',index=False, header=True,sep=',')




# ============================
# print("Mordred : " , dtMor.iloc[1].name) #gets all on row 
# print("Padel : " , dtPadel.iloc[1].Name) #gets all on row 0



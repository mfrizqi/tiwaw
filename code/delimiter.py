import csv 
import pandas as pd
import numpy as np

print('Hello Enjel!')

# with pandas
dtCdk = pd.read_csv("cdk_desc.csv", delimiter=' ')
dtHeadCdk = dtCdk.columns.values #get all CDK columns name

dtMor = pd.read_csv("mordred_desc.csv")
dtHeadMor = dtMor.columns.values #get all CDK columns name

dtPadel = pd.read_csv("padel_desc.csv")
dtHeadPad = dtPadel.columns.values #get all CDK columns name

dtRawIC50 = pd.read_csv("pIC50_target.csv")
dtIC50 = dtRawIC50['pIC50']

def last(self,n):
    return self.iloc[:,-n:]

def funcOne(numbers):
    print("Calling Function funcOne")
    print(numbers * 2)
    return

#Get data from csv
print(" ")
print("CDK index 1 title: " , dtCdk.iloc[1].Title) #gets data nrow on column series
# print("")
print(dtHeadCdk[286]) #Get single CDK column name
# print("")
print(dtHeadMor[1561]) #Get single CDK column name
# print("")
print(dtHeadPad[1875]) #Get single CDK column name
print("")
# funcOne(10)

#concate all dataframe (Mordred,Padel,Cdk,Target)

conDfSet = pd.concat([dtMor, dtPadel, dtCdk, dtIC50], axis=1)
conDfDrop = conDfSet
print (conDfSet)

#split 4:1 mixed dataframe random (4 Train : 1 Test)
#ratio train = 0.8
#using sample
# TrainSetOne = conDaSet.sample(75)

# GET TRAIN SET USING FRAC 0.8 RATIO
#using frac
TrainSet = conDfSet.sample(frac=0.8, random_state=45)
# print(TrainSetTwo)
idxList = ( list(TrainSet.index.values))
# print(len(idxList))
# print(type(idxList))

# print (TrainSet)

# print (TestSet)
# GET TEST SET BY DROP ROWS BASED TRAINSET ROWS
TestSet = conDfDrop.drop(idxList)

#CHECK BOTH DATAFRAME
print("----- TRAIN SET -----")
print(TrainSet)
print("")
print("")
print("")
print("----- TRAIN SET -----")
print(TestSet)

#EXPORT TRAIN&TEST SET TO CSV

TrainSet.to_csv (r'D:\Code\python\pandas\Exercise\TrainSet.csv',index=False, header=True, sep=',') #Don't forget to add '.csv' at the end of the path
TestSet.to_csv (r'D:\Code\python\pandas\Exercise\TestSet.csv',index=False, header=True,sep=',')


























# ============================
# print("Mordred : " , dtMor.iloc[1].name) #gets all on row 
# print("Padel : " , dtPadel.iloc[1].Name) #gets all on row 0



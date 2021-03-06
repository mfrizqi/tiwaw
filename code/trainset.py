from scipy.stats.stats import pearsonr
import os
import csv 
import pandas as pd
import statistics as stat
import numpy as np
import math

#Utility (Optional)
clear = lambda: os.system('cls')
clear()

#STEP 1 : COUNT ALL SIMILARITIES IN 1 ROW
#STEP 2 : IF COUNTED SIMILARITIES MORE THAN 37, DELETE COLUMN

dtTrain = pd.read_csv("data/TrainSetNoId.csv")
dtTrainRaw = dtTrain
# dtCdk = pd.read_csv("data/cdk_desc.csv", delimiter=' ')

def similarValue(dframe):
    colList = [] #List for column
    # colDframe = dframe.columns.values #get all columns
    for j in range(0,dframe.shape[1]):
        topEl = stat.mode(dframe.iloc[:,j]) # Get modus value from j column
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
    # colDframe = dframe.columns.values
    for j in range(0,dframe.shape[1]-1):
        # Loop search standard deviation each column
        stddev = 0
        sample = dframe.iloc[:,j] #Get all row in j column for standard deviation
        stddev = np.std(sample) #Get standard deviation from 'sample' list
        if stddev <= 0.95 :
            # print(j, "PICKED")
            stdevList.append(j)
    return stdevList

def checkNa(dframe):
    naList = []
    # colDframe = dframe.columns.values
    for j in range(0,dframe.shape[1]):
        cknan = dframe.iloc[0,j]
        if math.isnan(cknan): #Check NaN value at row 0 in column j
            naList.append(j)
    return naList

def checkInf(dframe):
    infList = []
    colDframe = dframe.columns.values
    for j in range(0,len(colDframe)):
        cknan = dframe.iloc[0,j]
        if math.isinf(cknan): #Check NaN value at row 0 in column j
            infList.append(j)
    return infList

def checkDupLabel(dframe):
    dupLabel = []
    for i in range(0,dframe.shape[1]):
        label = dframe.columns.values[i]
        for j in range(i+1, dframe.shape[1]):
            if(label == dframe.columns.values[j]):
                print(0)
    return dupLabel

def lowCorrP(dframe):
    label_ = dframe.columns.values
    pic50 = dframe.iloc[:,-1]
    corr_y = [pearsonr(dframe.iloc[:,i],pic50) for i in range(dframe.shape[1])]
    corr_y = [np.abs(corr_y[i][0]) for i in range(dframe.shape[1])]
    corr_lim = 0.20
    hi_corr = []
    for i in range(len(corr_y)):
        if corr_y[i] > corr_lim:
            hi_corr.append(i)
    label_idx = label_[hi_corr]
    dtLowCorr = dframe.loc[:,label_idx]
    # print(X_train)
    print("descriptor number after removing low correlation with target: {}".format(dtLowCorr.shape[1]))
    return dtLowCorr

def highCorrP(dframe):
    # -----------REMOVE FEATURE WITH HIGH CORRELATION TO OTHER FEATURE---------------------
    # re-calculate correlation with pic50
    label_ = dframe.columns.values
    pic50 = dframe.iloc[:,-1]
    corr_y = [pearsonr(dframe.iloc[:,i],pic50) for i in range(dframe.shape[1])]
    corr_y = [np.abs(corr_y[i][0]) for i in range(dframe.shape[1])]
    desc_num = dframe.shape[1]
    # calculate correlation for each descriptor
    corr_matrix = np.corrcoef(dframe.T)
    corr_lim = 0.80
    low_corr = np.arange(desc_num).tolist()
    tmp = np.arange(desc_num).tolist()
    for i in np.arange(desc_num):
        tmp.remove(i)
        for j in tmp:
            corr_ = np.abs(corr_matrix[i,j])
            if corr_ >= corr_lim:
                if corr_y[i] > corr_y[j]:
                    if j in low_corr:
                        low_corr.remove(j)
                else:
                    if i in low_corr:
                        low_corr.remove(i)
    label_idx = label_[low_corr]
    dtHiCorr = dframe.loc[:,label_idx]
    print("descriptor number after removing high correlation descriptor: {}".format(dtHiCorr.shape[1]))
    return dtHiCorr

def dropColumn(dframe, tList):
    dropped = pd.DataFrame() #Create empty dataframe
    dropped = dframe.drop(dframe.columns[tList], axis=1) #drop column based on list by column
    return dropped

########## START HERE ##########
#Create Nan Values List
naValues = []
print("#Trainset After Concatenated : ", dtTrain.shape[1]")

##### STEP 0 Reduces NAN Values
raw = len(dtTrain.columns)
dtTrain.dropna(axis=1, how='any', thresh=None, subset=None, inplace=True)
print("#0. Trainset ", dtTrain.shape[1] , " | ", raw-dtTrain.shape[1], " NaN value columns removed")

##### STEP 1 Reduces similarity
simValList = similarValue(dtTrain)
print("#1. Trainset ", dtTrain.shape[1] , " | ", dtTrain.shape[1] - len(simValList) , " similarity value columns removed")
dtTrain = dropColumn(dtTrain,simValList)

##### STEP 2 Reduce columns by Standard Deviation
sdList = stdDeviation(dtTrain)
print("#2. Trainset ", dtTrain.shape[1] , " | ", dtTrain.shape[1] - len(sdList) , " standard deviation below 0.95 value columns removed")
dtTrain = dropColumn(dtTrain,sdList)

###### STEP 3  Low Correlations
dtTrain = lowCorrP(dtTrain)

###### STEP 4 High Correlations
dtTrain = highCorrP(dtTrain)

print(dtTrain)


#+++++++++++++++ PLAYGROUND HERE (Test your code below this sign) +++++++++++++++#

# colDframe = dtStdList.columns.values
# for m in range(0,2):
#     xList = dtStdList.iloc[:,m]
#     for k in range(m+1,len(colDframe)):
#         # yName = dframe.columns.values[k]
#         yList = dtStdList.iloc[:,k]
#         pears = np.corrcoef(xList,yList)
#         print(pears)

# p = dtStdList.iloc[:,0]
# q = dtStdList.iloc[:,32]
# pears = np.corrcoef(p,q)
# print(type(pears))
# print (pears[0])
# print (pears[0][1])

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

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

cdkFirst = dtCdk.loc[:,(dtColCdk[0])]
morFirst = dtMor.loc[:,(dtColMor[0])]
padFirst = dtPadel.loc[:,(dtColPad[0])]

mixedFirst = pd.concat([cdkFirst,morFirst,padFirst], axis = 1)

mixedData= pd.concat([dtMor, dtPadel, dtCdk, dtIC50], axis=1)

del mixedData[(dtColCdk[0])]
del mixedData[(dtColMor[0])]
del mixedData[(dtColPad[0])]

completeData = pd.concat([mixedFirst,mixedData],axis = 1)

completeData.to_csv (r'D:\Perkuliahan\SEMESTER 8\tiwaw\code\completeData.csv',index=False, header=True, sep=',') #Don't forget to add '.csv' at the end of the path

# print(completeData.iloc[:,0:3778])
# print (completeData.iloc[92].pIC50)



# print(morFirst)
# print(padFirst)

# print(mixedData)
# print(type(mixedFirst))


# print(dtCdk.loc[:,(dtColCdk[0])])
# print(dtCdk.loc[2,(dtColCdk[0])])

print(completeData.loc[:,'Wgamma1.unity'])
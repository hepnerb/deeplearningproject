import numpy as np
import pandas as pd

okdata = pd.read_excel('CleanedDL.xlsx')
okdata = okdata.iloc[:,1:]
branddummies = pd.get_dummies(okdata.iloc[:,1], drop_first=True)
okdata = pd.concat([okdata, branddummies], axis=1)
okdata = okdata.drop(columns=['Brand'])
test = pd.concat([okdata.iloc[10:11],okdata.iloc[16:17],okdata.iloc[20:21],okdata.iloc[25:26],okdata.iloc[45:46]])
okdata = okdata.drop([10,16,20,25,45], axis=0)
test.to_csv('test_data.csv')
okdata.to_csv('train_data.csv')
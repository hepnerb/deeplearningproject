import numpy as np
import pandas as pd

okdata = pd.read_excel('CleanedDL.xlsx')
okdata = okdata.iloc[:,0:]
branddummies = pd.get_dummies(okdata.iloc[:,2], drop_first=True)
okdata = pd.concat([okdata, branddummies], axis=1)
okdata = okdata.drop(columns=['Brand'])
print(okdata.iloc[:,1:])
okdata.to_csv('CleanedDL.csv')
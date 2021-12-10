import numpy as np
import pandas as pd

okdata = pd.read_excel('CleanedDL.xlsx')
okdata = okdata.iloc[:,1:]
branddummies = pd.get_dummies(okdata.iloc[:,1], drop_first=True)
okdata = pd.concat([okdata, branddummies], axis=1)
okdata = okdata.drop(columns=['Brand'])
okdata.to_csv('CleanedDL.csv')
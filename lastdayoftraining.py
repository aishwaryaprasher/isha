#question1
import numpy as np
import pandas as pd
data={'NAME':['Aishwarya'],'age':[21],'mail id':['ashwaryaprasher@gmail.com'],'phone no.':[9999999999]}
df=pd.DataFrame(data)
print(df)
df.loc[1]=['tom',22,'jerry@gmail.com',9876789898]
print(df)

#question1
import numpy as np
import pandas as pd
data={'NAME':['Aishwarya'],'age':[21],'mail id':['ashwaryaprasher@gmail.com'],'phone no.':[9999999999]}
df=pd.DataFrame(data)
print(df)
df.loc[1]=['tom',22,'jerry@gmail.com',9876789898]
print(df)

#question2

import numpy as np
import pandas as pd
data=pd.read_csv("weather.csv")
df=pd.DataFrame(data)
print("First five rows")
print(df.head(5))
print("First ten rows")
print(df.head(10))
print("Basic statistics")
print("Axes-\n"+str(df.axes))
print("Datatypes-\n"+str(df.dtypes))
print("Dimensons-\n"+str(df.ndim))
print("Shape-\n"+str(df.shape))
print("Size\n"+str(df.size))
print("\n")
print("Last five rows")
print(df.tail(5))


x=df.loc[:,'Location']
print(x)
print("Basic statistics")
print("Axes-\n"+str(x.axes))
print("Datatypes-\n"+str(x.dtypes))
print("Dimensons-\n"+str(x.ndim))
print("Shape-\n"+str(x.shape))
print("Size\n"+str(x.size))
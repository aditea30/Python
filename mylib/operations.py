#operations on series
('''import pandas as pd
s=pd.Series([0,2,4,6,7])
print("Multiply all the elements with 2")
print(s*2)
print("Squaring all the elements persent")
print(s*s)
print("Elements greater than 2")
print(s[s>2])

#operations on different series
import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
s2=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s3=pd.Series([5,10,15,20],index=['a','b','c','d'])
print("Adding series s & s2")
print(s+s2)
print("Adding series s2 & s3")
print(s2+s3)
print("Adding series s2 & s3 printing 0 if index not found")
print(s2.add(s3,fill_value=0))''')

#Head and tail functions in python
import pandas as pd
import numpy as np
arr=np.array([10,45,78,44,7,4,2])
s=pd.Series(arr)
print(s.head()) #if no parameter is given it prints first 5 rows only

print(s.tail(6))#last 5 rows only

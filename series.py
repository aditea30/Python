#create series with ndarray
import pandas as pd
import numpy as np
arr=np.array([10,15,18,22])
s=pd.Series(arr)
print(s)

#seies with mutable index
import pandas as pd
import numpy as np
arr=np.array(['a','b','c','d'])
s=pd.Series(arr,index=['first','second','third','fourth'])
print(s)

#creating series using scalar value
import pandas as pd
s=pd.Series(50,index=['10','20','30','40'])
print(s)

#creating a series using dictionaries
import pandas as pd
d={'1':'Jan','2':'Feb','3':'March'}
s=pd.Series(d)
print(s)

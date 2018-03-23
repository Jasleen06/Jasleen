
# coding: utf-8

# In[10]:

import pandas as pd

a=pd.read_csv("C:\\Users\\JASLEEN\\Documents\\jobs\\L3 test\\patent_drawing.csv")
a


# In[11]:

import pandas as pd
df = pd.DataFrame(a)
c=(df[df.text.str.contains('embod')].count())
c


# 1312 out of the total descriptions mention words having the stem word 'embod-'

# In[12]:

df = pd.DataFrame(a)
d=(df[df.text.str.contains('embod') & df.text.str.contains('invention')].count())
d


# 901 out of the total descriptions mention 'embod(with any ending) followed by invention'

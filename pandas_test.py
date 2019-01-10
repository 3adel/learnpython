import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style 
style.use('ggplot')

#a data frame is a dictionary at its heart 
web_stats = {'Day': [1,2,3,4,5,6],
			 'Visitors':[43,55,76,34,43,77],
			 'Bounce_rate':[65, 72, 62, 64, 54, 88]}

df = pd.DataFrame(web_stats).set_index('Day')

print(">>> Entire data frame",df)
print(">>> Head of data frame",df.head())
print(">>> Tail of data frame",df.tail())


#now I set the index

#accessing a column 
print(df['Visitors'])





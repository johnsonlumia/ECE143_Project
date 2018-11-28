import pandas as pd
import matplotlib.pyplot as plt

#Department to analyze
department = 'ucsd_cse'

#keywords to analyze
keyword0 = 'computer architecture'
keyword1 = 'data structures'
keyword2 = 'machine learning'
keyword3 = 'storage systems'
keyword4 = 'information technology'

cse_df = pd.read_excel(department + '.xlsx')

cse_df.loc[keyword0].plot()
cse_df.loc[keyword1].plot()
cse_df.loc[keyword2].plot()
cse_df.loc[keyword3].plot()
cse_df.loc[keyword4].plot()
plt.savefig(department + "_plot")
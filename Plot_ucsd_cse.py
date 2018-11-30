# ECE 143 Engineering Course Analysis
# Plots of selected catalog topics from the UCSD CSE Department
#
# matplotlib ONLY version, WORK IN PROGRESS
# python and plotly used for presentation
#
# By Fernando Lopez

import pandas as pd
import matplotlib.pyplot as plt

# Department to analyze
department = 'ucsd_cse'

# keywords to analyze
keyword0 = 'computer architecture'
keyword1 = 'data structures'
keyword2 = 'machine learning'
keyword3 = 'storage systems'
keyword4 = 'information technology'

# Read excel file into a Data Frame
cse_df = pd.read_excel(department + '.xlsx')

# Plot the ocurrences of the selected keywords
cse_df.loc[keyword0].plot()
cse_df.loc[keyword1].plot()
cse_df.loc[keyword2].plot()
cse_df.loc[keyword3].plot()
cse_df.loc[keyword4].plot()

plt.title("UCSD CSE Skills Promoted")
plt.xlabel('Year')
plt.ylabel('Ocurrences')
plt.ylim(0, 18,)
plt.savefig(department + "_all" + "_plot")
plt.cla()

# Plot top performers
cse_df.loc[keyword0].plot()
cse_df.loc[keyword1].plot()

plt.title("UCSD CSE Top Performers")
plt.xlabel('Year')
plt.ylabel('Ocurrences')
plt.ylim(0, 18)
plt.savefig(department + "_top" + "_plot")
plt.clf()

# Plot rising stars
cse_df.loc[keyword2].plot()

plt.title("UCSD CSE Rising Star")
plt.xlabel('Year')
plt.ylabel('Ocurrences')
plt.ylim(0, 18)
plt.savefig(department + "_rising" + "_plot")
plt.clf()

# Plot bottom performers
cse_df.loc[keyword3].plot()
cse_df.loc[keyword4].plot()

plt.title("UCSD CSE Bottom Performers")
plt.xlabel('Year')
plt.ylabel('Ocurrences')
plt.ylim(0, 18)
plt.savefig(department + "_down" + "_plot")
plt.clf()

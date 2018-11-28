# This script is used to plot data from analysis
# Department by department
# Hard code is used for the topics has been choosen from the most
# frequently mentioned in the catalog
# !!!Plot data only script!!!

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
import os

# Page 14 ECE
df = pd.read_excel(os.path.join('processed_data','ece.xlsx'), index_col=0, usecols = "A:N")
integrated = df.loc['integrated circuits']
communication = df.loc['communication systems']
machine = df.loc['machine learning']
data_a = df.loc['data analysis']

years = np.linspace(2006,2018, 13, dtype=np.int64)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(years, integrated,'bo-')
ax.plot(years, communication,'go-')
ax.plot(years, machine,'ro-')
ax.plot(years, data_a,'yo-')
ax.set_ylabel('word freqency')
ax.set_xlabel('catalog year')
ax.set_title('ECE Page14')
ax.legend()

fig.show()

# Page 15 ECE
df = pd.read_excel(os.path.join('processed_data','ece.xlsx'), index_col=0,usecols = "A:N")
sp = df.loc['signal processing']
ic = df.loc['integrated circuits']
sd = df.loc['system design']
ml = df.loc['machine learning']
da = df.loc['data analysis']
years = np.linspace(2006,2018, 13, dtype=np.int64)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(years, sp,'bo-')
ax.plot(years, ic,'go-')
ax.plot(years, sd,'ro-')
ax.plot(years, ml,'yo-')
ax.plot(years, da,'co-')
ax.set_ylabel('word freqency')
ax.set_xlabel('catalog year')
ax.set_title('ECE Page15')
ax.legend()

fig.show()

# Page 14 CSE
df = pd.read_excel(os.path.join('processed_data','cse.xlsx'), index_col=0,usecols = "A:N")
data_structures = df.loc['data structures']
distributed = df.loc['distributed systems']
machine = df.loc['machine learning']
data_sci = df.loc['data science']

years = np.linspace(2006,2018, 13, dtype=np.int64)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(years, data_structures,'bo-')
ax.plot(years, distributed,'go-')
ax.plot(years, machine,'ro-')
ax.plot(years, data_sci,'yo-')
ax.set_ylabel('word freqency')
ax.set_xlabel('catalog year')
ax.set_title('CSE Page14')
ax.legend()

fig.show()

# Page 16 CSE
df = pd.read_excel(os.path.join('processed_data','cse.xlsx'), index_col=0,usecols = "A:N")
ds = df.loc['data structures']
cv = df.loc['computer vision']
ml = df.loc['machine learning']
cg = df.loc['computer graphics']
dm = df.loc['data mining']
ds = df.loc['data science']

years = np.linspace(2006,2018, 13, dtype=np.int64)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(years, ds,'bo-')
ax.plot(years, cv,'go-')
ax.plot(years, ml,'ro-')
ax.plot(years, cg,'yo-')
ax.plot(years, dm,'co-')
ax.plot(years, ds,'mo-')
ax.set_ylabel('word freqency')
ax.set_xlabel('catalog year')
ax.set_title('CSE Page16')
ax.legend()

fig.show()

# Page 14 ME
df = pd.read_excel(os.path.join('processed_data','me.xlsx'), index_col=0,usecols = "A:N")
ms = df.loc['mechanical systems']
marine = df.loc['marine structures']
cd = df.loc['control design']
hs = df.loc['hybrid systems']

years = np.linspace(2006,2018, 13, dtype=np.int64)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(years, ms,'bo-')
ax.plot(years, marine,'go-')
ax.plot(years, cd,'ro-')
ax.plot(years, hs,'yo-')
ax.set_ylabel('word freqency')
ax.set_xlabel('catalog year')
ax.set_title('ME Page14')
ax.legend()

fig.show()

# Page 17 ME
df = pd.read_excel(os.path.join('processed_data','me.xlsx'), index_col=0,usecols = "A:N")
cs = df.loc['control systems']
fe = df.loc['finite element']
fd = df.loc['fluid dynamics']
ds = df.loc['dynamical systems']
cd = df.loc['control design']
hs = df.loc['hybrid systems']


years = np.linspace(2006,2018, 13, dtype=np.int64)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(years, cs,'bo-')
ax.plot(years, fe,'go-')
ax.plot(years, fd,'ro-')
ax.plot(years, ds,'yo-')
ax.plot(years, cd,'co-')
ax.plot(years, hs,'mo-')
ax.set_ylabel('word freqency')
ax.set_xlabel('catalog year')
ax.set_title('ME Page17')
ax.legend()

fig.show()
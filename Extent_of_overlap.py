#
# Visualization part 3 
# Script that deals with Extent of overlap, using Venn Diagrams 
#
# Nov 25, 2018 by Ambareesh S J
# 
#

import pandas as pd
import itertools as it
from matplotlib_venn import venn2,venn3
import matplotlib.pyplot as plt
from matplotlib.pylab import subplots

def make_venn_diagram(set_a,set_b,title_of_plot='UCSD'):
	'''
	Function that creates a venn diagram representation of ECE and CSE Departments and portrays the extent of overlap between them
	
	'''
    labels_depts=['CSE','ECE']
    total = len(set_a.union(set_b))
    v1 = venn2([set_a,set_b],set_labels=labels_depts,set_colors=['red','green'],subset_label_formatter=lambda x: f"{(x/total):1.0%}")
    plt.title(title_of_plot)
    return v1
	
plt.subplot(221) #making 2*2 subplots for 4 different plots (4 universities)
df1=pd.read_excel('ucberkeley_cs.xlsx',usecols='A')
cse_set_ucb = set(list(it.chain.from_iterable(df1.values.tolist())))
df2 = pd.read_excel('ucberkeley_ee.xlsx',usecols='A')
ece_set_ucb = set(list(it.chain.from_iterable(df2.values.tolist())))
make_venn_diagram(cse_set_ucb,ece_set_ucb,title_of_plot='UCB')

plt.subplot(222)
df1=pd.read_excel('ucla_cse.xlsx',usecols='A')
cse_set_ucla = set(list(it.chain.from_iterable(df1.values.tolist())))
df2 = pd.read_excel('ucla_ece.xlsx',usecols='A')
ece_set_ucla = set(list(it.chain.from_iterable(df2.values.tolist())))
make_venn_diagram(cse_set_ucla,ece_set_ucla,title_of_plot='UCLA')

plt.subplot(223)
df1=pd.read_excel('ucsb_cse.xlsx',usecols='A')
cse_set_ucsb = set(list(it.chain.from_iterable(df1.values.tolist())))
df2 = pd.read_excel('ucsb_ece.xlsx',usecols='A')
ece_set_ucsb = set(list(it.chain.from_iterable(df2.values.tolist())))
make_venn_diagram(cse_set_ucsb,ece_set_ucsb,title_of_plot='UCSB')

plt.subplot(224)
df1=pd.read_excel('ucsd_cse.xlsx',usecols='A')
cse_set_ucsd = set(list(it.chain.from_iterable(df1.values.tolist())))
df2 = pd.read_excel('ucsd_ece.xlsx',usecols='A')
ece_set_ucsd= set(list(it.chain.from_iterable(df2.values.tolist())))
make_venn_diagram(cse_set_ucsd,ece_set_ucsd,title_of_plot='UCSD')

plt.show()
# This script connect industry hot topics with universities
# We got Industry_words.txt which is analyzed using the script analyze_data_merge_industry.py
# Then this script checks if the words from Industry_words.txt has frequency in Universities'
# catalog. Which produce a excel file industry_connection.xlsx
# Strat from line 91, we used analyzed excel sheet to finde the hot topics
# which has data from all the four universities.
# Radar chart is drawn by using matplotlib.
import os
import sqlite3
import pandas as pd
import numpy as np
from math import pi
import matplotlib.pyplot as plt

industry_words = []
with open(os.path.join('scripts', 'Industry_words.txt'), 'rt') as f:
    for line in f.readlines():
        industry_words.append(line.strip('\n'))
df_rowindex = industry_words
with sqlite3.connect(os.path.join('processed_data','Analyzed_data.db')) as con:
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablename = cursor.fetchall()
    tablename = list(map(lambda i: i[0].split('_'), tablename))
    school_list = []
    for name in tablename:
        #name[0] is school, name[1] is department
        school_list.append(name[0])
    school_list = list(set(school_list))
    df_columnindex = school_list
    freq_array = np.zeros([len(industry_words), len(school_list)])
    for iword in industry_words:
        for school in school_list:
            # Due to raw data file name provided by Fernando,
            # Some condition assignment should be placed :(
            if school == 'ucberkeley':
                ece = 'ee'
                cse = 'cs'
            else:
                ece = 'ece'
                cse = 'cse'
            df_ece = pd.read_sql_query(
                "SELECT * FROM "+str('_'.join([school, ece])), con=con)
            df_cse = pd.read_sql_query(
                "SELECT * FROM "+str('_'.join([school, cse])), con=con)
            for bigram in df_cse['index']:
                if iword in bigram:
                    df_index = list(df_cse['index']).index(bigram)
                    freq_array[industry_words.index(iword), school_list.index(school)] = freq_array[industry_words.index(
                        iword), school_list.index(school)]+df_cse['18'][df_index]
            for bigram in df_ece['index']:
                if iword in bigram:
                    df_index = list(df_ece['index']).index(bigram)
                    freq_array[industry_words.index(iword), school_list.index(school)] = freq_array[industry_words.index(
                        iword), school_list.index(school)]+df_ece['18'][df_index]
df = pd.DataFrame(freq_array, df_rowindex, df_columnindex)
df.to_excel(os.path.join('processed_data','industry_connection.xlsx'), sheet_name='result')
# We examine the output excel file to find the five hot topics which have frequency overlap among
# four universities.
# Then we have the subject_list to draw the radar chart
subject_list = ['machine learning', 'signal processing', 'data structures', 'circuit design',
                'system design']
df = df.loc[subject_list]

# Draw radar chart
# number of variable
categories = ['\n'.join(word.split(' ')) for word in subject_list]
N = len(categories)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
size = len(school_list)
# Four schools' color
colormap = ['r', 'g', 'b', 'c']


def draw_radar_chart(n, values):
    ax = plt.subplot(2, 2, n+1, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories, fontsize=18)
    # Offset the subject words
    ax.tick_params(direction='out', pad=23)
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=9)
    # Limit of the outter circle
    plt.ylim(0, 20)
    # Plot&Fill radar chart
    ax.plot(angles, values,
            color=colormap[i], linewidth=1, linestyle='solid', label=school_list[i])
    ax.fill(angles, values, colormap[i], alpha=0.1)
    plt.legend(loc='upper right', bbox_to_anchor=(-0.1, 0.1), fontsize=20)


for i in range(len(school_list)):
    values = df[school_list[i]].values.flatten().tolist()
    values += values[:1]
    draw_radar_chart(i, values)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                    wspace=None, hspace=0.3)
plt.show()

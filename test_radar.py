# ------- PART 1: Create background

# number of variable
categories = subject_list
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
def draw_radar_chart(n, size, angles, values):
    # Initialise the spider plot
    ax = plt.subplot(1,size,n+1, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
    plt.ylim(0, 20)


    ax.plot(angles, values, linewidth=1, linestyle='solid', label=school_list[i])
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
for i in range(len(school_list)):
    values = df[school_list[i]].values.flatten().tolist()
    values += values[:1]
    draw_radar_chart(i,len(school_list),angles,values)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=5, hspace=None)
plt.show()
# freq_df.to_excel('industry_connection.xlsx',sheet_name='result')

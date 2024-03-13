import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# pandas read xlsx
source = 'happy_stand'
file_path = r'./excel/Data_temp.xlsx'
df = pd.read_excel(file_path, sheet_name='无噪声')  

#根据source选取数据
match source:
    case 'angel':
        df = df.iloc[0:6] 
    case 'Armadillo_scans':
        df = df.iloc[9:15] 
    case 'bunny':
        df = df.iloc[17:23]
    case 'dragon_stand':
        df = df.iloc[25:31]
    case 'hand':
        df = df.iloc[33:39]
    case 'happy_stand':
        df = df.iloc[41:47]
    case _:
        print("source path input error!")

print(df)

# 取每行的ET值
cluster_et, icp_et, p2plane_et, robust_et, aa_et, trimmed_et = df.loc[:,['ET','ET.1','ET.2','ET.3','ET.4','ET.5']].values

# x轴刻度标签
x_ticks = ['5', '10', '15', '20', '25','30']
# x轴范围（0, 1, ..., len(x_ticks)-1）
x = np.arange(len(x_ticks))
fig, ax = plt.subplots()

# Cluster:画第1条折线，参数看名字就懂，还可以自定义数据点样式等等。
line_cluster, = plt.plot(x, cluster_et, color='#E6A4B4', label='cluster', linewidth=3.0,marker="o")
# Standard icp:画第2条折线
line_standard, = plt.plot(x, icp_et, color='#D4E2D4', label='standard', linewidth=3.0,marker="o")
# p2plane icp
line_p2plane, = plt.plot(x, p2plane_et, color='#96B6C5', label='p2plane', linewidth=3.0,marker="o")
#robust icp
line_robust, = plt.plot(x, robust_et, color='#FF8080', label='robust', linewidth=3.0,marker="o")
#aa_icp
line_aa, = plt.plot(x, aa_et, color='#FFCF96', label='aa', linewidth=3.0,marker="o")
#trimmed icp
line_tr, = plt.plot(x, trimmed_et, color='#7469B6', label='trimmed', linewidth=3.0,marker="o")

lines = [line_cluster,line_standard,line_p2plane,line_robust,line_aa,line_tr]

annot = ax.annotate("", xy=(0,0), xytext=(-20,20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind, line_num):
    x_data, y_data = lines[line_num].get_data()
    annot.xy = (x_data[ind["ind"][0]], y_data[ind["ind"][0]])
    text = "{:.8f}".format(y_data[ind["ind"][0]])
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        for i, line in enumerate(lines):
            cont, ind = line.contains(event)
            if cont:
                update_annot(ind, i)
                annot.set_visible(True)
                fig.canvas.draw_idle()
                return
    if vis:
        annot.set_visible(False)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

# 添加x轴和y轴刻度标签
plt.xticks([r for r in x], x_ticks, fontsize=18, rotation=20)
plt.yticks(fontsize=18)

# 添加x轴和y轴标签
plt.xlabel(u'Rot degree of Source Cloud', fontsize=18)
plt.ylabel(u'Translation Error', fontsize=18)

# 标题
file_title = source + ': ET - Rot_degree'
plt.title(file_title, fontsize=18)

# 图例
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0)
plt.tight_layout()

# 网格线
plt.grid()

# 保存图片
fig_path = './pic/' + source +'/' + source + '_ET_rot_degree.png'
plt.savefig(fig_path, bbox_inches='tight')

# 显示图片
plt.show()
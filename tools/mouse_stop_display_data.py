import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

x = np.sort(np.random.rand(15))
y1 = np.sort(np.random.rand(15))
y2 = np.sort(np.random.rand(15))
names = np.array(list("ABCDEFGHIJKLMNO"))

norm = plt.Normalize(1,4)
cmap = plt.cm.RdYlGn

fig, ax = plt.subplots()
line1, = plt.plot(x, y1, marker="o", label='Line 1')
line2, = plt.plot(x, y2, marker="o", label='Line 2')
lines = [line1, line2]

annot = ax.annotate("", xy=(0,0), xytext=(-20,20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind, line_num):
    x_data, y_data = lines[line_num].get_data()
    annot.xy = (x_data[ind["ind"][0]], y_data[ind["ind"][0]])
    text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
                        " ".join([names[n] for n in ind["ind"]]))
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

plt.legend()
plt.show()

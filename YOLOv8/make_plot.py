import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys


class Make_plot():
    def __init__(self, filename, sheet_name, labels, colors, show_legend=True, use_grid=False):
        self.filename = filename
        self.data_dict = pd.read_excel(self.filename, sheet_name=None)
        self.sheet_name = sheet_name
        self.labels = labels
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文为宋体
        plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 英文为新罗马
        plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
        plt.rcParams['font.size'] = 20  # 设置字号
        # self.fig, self.ax = plt.subplots(figsize=(18, 6))
        self.lines = 0
        self.show_legend = show_legend
        self.use_grid = use_grid
        self.colors = colors
        self.current_color_index = 0

        # print(self.data_dict)

    def make_line_chart(self, save_path, color=None, ):
        # if color is None:
        #     color = self.colors
        for i in range(1, 11):
            fig, ax = plt.subplots(figsize=(6, 6), dpi=400)
            sheet_name = self.sheet_name
            label = self.labels
            color = self.colors  # 直接替换颜色即可改变线条颜色和标记点颜色
            for key, label, color in zip(sheet_name, label, color):
                print(key, label, color)
                sheet = self.data_dict[key]
                columns_name = sheet.columns
                epoch = sheet[columns_name[0]].values
                # ax.set_title(columns_name[i])
                ax.set_xlabel('Epoch', fontweight='bold')
                ax.set_ylabel(columns_name[i], fontweight='bold')
                ax.set_ylim(0,0.80)
                ax.plot(epoch, sheet[columns_name[i]].values, 'o--', linewidth=1, label=label,
                        markersize=2, color=color, markeredgecolor=color,
                        markerfacecolor=color)
                plt.legend(loc='lower right',prop={'size': 15})
                plt.grid(visible=True, which='major', linestyle='-')
                plt.grid(visible=True, which='minor', linestyle='--', alpha=0.5)
                plt.minorticks_on()
            plt.savefig(save_path + '\\' + columns_name[i], bbox_inches='tight', dpi=400)


# plt.style.use(['science','no-latex'])
# 需要需要进行绘制的工作表名称
# sheet_name = ['8n_result', '8s_result', '8m_result', '8l_result']
sheet_name = ['8n_result', '8s_result', '8m_result', '8l_result']
# 绘制的对象标签
labels = ['YOLOv8n', 'YOLOv8s', 'YOLOv8m', 'YOLOv8l']
# 直接替换颜色即可改变线条颜色和标记点颜色
colors = ['royalblue', 'darkorange', 'seagreen', 'crimson']
# colors = ['#CD76AB', "#FFCCOO", "#52B6E6", "#3EBOA2"]
# 创建绘制对象
plot = Make_plot(r'C:\Users\Administrator\Desktop\基于YOLO深度学习的城市公交车洪涝识别\结果分析1010.xlsx',sheet_name,labels,colors)
# 设置保存路径
save_path = r'C:\Users\Administrator\Desktop\基于YOLO深度学习的城市公交车洪涝识别\论文图片'
plot.make_line_chart(save_path)

# .\venv\Scripts\activate
#  yolo task=detect mode=train model=yolov8l.pt data=data.yaml epochs=50 imgsz=640 batch=16 workers=8 device=0

from ultralytics import YOLO
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置中文字体为宋体, 英文标签使用新罗马字体
mpl.rcParams['axes.labelsize'] = 16  # 坐标轴标签字体大小
mpl.rcParams['axes.labelweight'] = 'bold'  # 坐标轴标签加粗
mpl.rcParams['axes.titlesize'] = 20  # 图表标题字体大小
mpl.rcParams['axes.titleweight'] = 'bold'  # 图表标题加粗
mpl.rcParams['xtick.labelsize'] = 14  # X轴刻度字体大小
mpl.rcParams['ytick.labelsize'] = 14  # Y轴刻度字体大小
mpl.rcParams['xtick.major.width'] = 1.5  # X轴刻度线宽
mpl.rcParams['ytick.major.width'] = 1.5  # Y轴刻度线宽
mpl.rcParams['axes.linewidth'] = 1.5  # 坐标轴线宽
mpl.rcParams['figure.dpi'] = 400  # 设置全局 DPI 为 300
mpl.rcParams['legend.loc'] = 'lower left'  # 图例位置：左下角
mpl.rcParams['legend.frameon'] = False  # 移除图例边框
mpl.rcParams['legend.fontsize'] = 12  # 图例字体大小

# Load a model
model = YOLO(r'E:\Anaconda\envs\yolov8\ultralytics-main\runs\detect\train4_8l_epochs100_strengthened\weights\best.pt')  # build a new model from YAML
# # Train the model
results = model.val(data='yolov8-bus-strengthened.yaml', imgsz=640, batch=16, workers=6)

# Load a model
# model = YOLO(r"E:\Anaconda\envs\yolov8\ultralytics-main\runs\detect\train2\weights\last.pt")  # load a partially trained model
# # # Resume training
# results = model.train(resume=True)

# https://www.anaconda.com/download/successd
from ultralytics import YOLO


# Load a model
# model = YOLO(r"E:\Anaconda\envs\yolov8\ultralytics-main\runs\detect\train2_8l_epoch100\weights\best.pt")  # load a pretrained model (recommended for training)
# model = YOLO(r"E:\Anaconda\envs\yolov8\ultralytics-main\runs\detect\train5_8l_epochs100_strengthened\weights\best.pt")  # load a pretrained model (recommended for training)
model = YOLO(r"C:\Users\wobei\Desktop\YOLOv8训练结果\4.第四轮 无原数据集 增加修改验证集 四个模型效果都有提升\train4_8l_epochs100_strengthened\weights\best.pt")  # load a pretrained model (recommended for training)

#
# # Train the model
results = model.predict(r"E:\Anaconda\envs\yolov8\ultralytics-main\ultralytics\assets\2.jpg", save=True)

# Load a model
# model = YOLO(r"E:\Anaconda\envs\yolov8\ultralytics-main\runs\detect\train2\weights\last.pt")  # load a partially trained model
# # # Resume training
# results = model.train(resume=True)

# https://www.anaconda.com/download/successd
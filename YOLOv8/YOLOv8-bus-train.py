from ultralytics import YOLO

# Load a model
model = YOLO('yolov8s.yaml')  # build a new model from YAML
model = YOLO('yolov8s.pt')  # load a pretrained model (recommended for training)
#
# # Train the model
results = model.train(data='yolov8-bus-strengthened.yaml', epochs=100, imgsz=640, batch=16, workers=12)

# Load a model
# model = YOLO(r"E:\Anaconda\envs\yolov8\ultralytics-main\runs\detect\train2\weights\last.pt")  # load a partially trained model
# # # Resume training
# results = model.train(resume=True)

# https://www.anaconda.com/download/successd
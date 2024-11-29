import os
import random
import shutil

def moveFile(input1, input2, save1, save2):
    pathDir = os.listdir(input1)  # 取图片的原始路径
    random.seed(1)
    filenumber = len(pathDir)  # 原文件个数
    rate = 0.75  # 抽取的验证集的比例，占总数据的多少
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取需要数量的样本图片
    print(sample)
    list_len = len(sample)
    print(list_len)
    list = []
    for i in range(len(sample)):
        list.append(sample[i].split('.')[0])
    print(list)
    for flie_name in list:
        path_img = os.path.join(input1, flie_name + '.jpg')
        shutil.move(path_img, save1)
        path_lab = os.path.join(input2, flie_name + '.txt')
        shutil.move(path_lab, save2)


if __name__ == '__main__':
    input_path1 = r'C:\Users\wobei\Desktop\bus_strengthened_new0828\images\train'
    input_path2 = r'C:\Users\wobei\Desktop\bus_strengthened_new0828\labels\train'
    save_img = r'C:\Users\wobei\Desktop\bus_strengthened_new0828\images\val'
    save_lab = r'C:\Users\wobei\Desktop\bus_strengthened_new0828\labels\val'
    if not os.path.exists(save_lab):
        os.makedirs(save_lab)
    if not os.path.exists(save_img):
        os.makedirs(save_img)
    moveFile(input_path1, input_path2, save_img, save_lab)
import os
from collections import Counter

# 指定txt文件所在的文件夹路径
folder_path = r'C:\Users\Administrator\Desktop\labels'

# 初始化一个Counter用于统计标签类别的总数
label_counts = Counter()

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            # 逐行读取文件内容，获取每行的第一个数字作为标签类别
            for line in file:
                label = line.strip().split()[0]  # 只取第一个数字
                label_counts[label] += 1

# 打印每个标签类别的总数
for label, count in label_counts.items():
    print(f"标签类别 {label} 的总数为: {count}")

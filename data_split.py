#coding:utf-8
import random
import os

# 图像数量
n_train_val_kitta = 0
n_train_val_kitti = 7481
n_train_val = n_train_val_kitti+n_train_val_kitta
n_test = 7518

train_val = list(range(n_train_val_kitta)) + list(range(100000, 100000+n_train_val_kitti))
# 训练集所占比例
p_train=0.5
# 训练集数量
n_train = int(n_train_val*p_train)

train = random.sample(train_val, n_train)
train.sort()

val = list(set(train_val)-set(train))
val.sort()

test = list(range(n_test))


# print(len(val))


# 写入文件

if not os.path.exists('ImageSets'):
    os.mkdir('ImageSets')
    
names = ['test.txt', 'train.txt', 'trainval.txt', 'val.txt']
data = [test, train, train_val, val]

for i, name in enumerate(names):
    current_f = os.path.join('ImageSets', name)
    f = open(current_f, 'w')

    for j in data[i]:
        id = str(j).zfill(6)
        f.write(str(id)+'\n')
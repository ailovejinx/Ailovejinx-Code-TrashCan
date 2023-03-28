#coding:utf-8
import random
import os
import pandas as pd

# 图像数量
n_train_val_kitta = 18595
n_train_val_kitti = 7481
n_train_val = n_train_val_kitti+n_train_val_kitta
n_test = 7518

# 为实验A、B划分验证集/训练集，AB的验证集要保持一致
train_val_A = list(range(100000, 100000+n_train_val_kitti))
# 验证集所占比例
p_val = 0.5
n_val = int(n_train_val_kitti*p_val)

# 随机抽取验证集
val_A = random.sample(train_val_A, n_val)
val_A.sort()

train_A = list(set(train_val_A)-set(val_A))


train_val_B = list(range(n_train_val_kitta)) + \
    list(range(100000, 100000+n_train_val_kitti))
val_B = val_A
train_B = list(set(train_val_B)-set(val_B))

train_val_C = list(range(n_train_val_kitta))
val_C = val_A
train_C = list(set(train_val_C)-set(val_C))


# 只抽0.2的合成数据进行训练
p = 0.2
kitta_B_small = int(p*n_train_val_kitta)
train_val_B_small = list(random.sample(range(
    n_train_val_kitta), kitta_B_small))+list(range(100000, 100000+n_train_val_kitti))

# 保证B_small的val和前面的都一样
val_B_small = pd.read_csv('ImageSets_A/val.txt', sep=' ', index_col=False, names=['val'])

val_B_small = val_B_small['val'].tolist()
print(val_B_small)

train_B_small = list(set(train_val_B_small)-set(val_B_small))

test = list(range(n_test))

print('A_train: ', len(train_A))
print('A_val: ', len(val_A))
print('B_train: ', len(train_B))
print('B_val: ', len(val_B))
print('C_train: ', len(train_C))
print('C_val: ', len(val_C))
print('B_small_train: ', len(train_B_small))
print('B_small_val: ', len(val_B_small))


# 写入文件

if not os.path.exists('ImageSets_A'):
    os.mkdir('ImageSets_A')

if not os.path.exists('ImageSets_B'):
    os.mkdir('ImageSets_B')

if not os.path.exists('ImageSets_C'):
    os.mkdir('ImageSets_C')

if not os.path.exists('ImageSets_B_small'):
    os.mkdir('ImageSets_B_small')


names = ['test.txt', 'train.txt', 'trainval.txt', 'val.txt']
data_A = [test, train_A, train_val_A, val_A]
data_B = [test, train_B, train_val_B, val_B]
data_C = [test, train_C, train_val_C, val_C]
data_B_small = [test, train_B_small, train_val_B_small, val_B_small]

for i, name in enumerate(names):
    # current_f = os.path.join('ImageSets_A', name)
    # f = open(current_f, 'w')

    # for j in data_A[i]:
    #     id = str(j).zfill(6)
    #     f.write(str(id)+'\n')

    # current_f = os.path.join('ImageSets_B', name)
    # f = open(current_f, 'w')

    # for k in data_B[i]:
    #     id = str(k).zfill(6)
    #     f.write(str(id)+'\n')

    # current_f = os.path.join('ImageSets_C', name)
    # f = open(current_f, 'w')

    # for l in data_C[i]:
    #     id = str(l).zfill(6)
    #     f.write(str(id)+'\n')

    current_f = os.path.join('ImageSets_B_small', name)
    f = open(current_f, 'w')

    for l in data_B_small[i]:
        id = str(l).zfill(6)
        f.write(str(id)+'\n')

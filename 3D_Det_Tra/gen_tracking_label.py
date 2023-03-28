"""
  @ Author       : Ailovejinx
  @ Date         : 2023-03-28 14:58:10
  @ LastEditors  : Ailovejinx
  @ LastEditTime : 2023-03-28 16:46:43
  @ FilePath     : gen_tracking_label.py
  @ Description  : 
  @ Copyright (c) 2023 by Ailovejinx, All Rights Reserved. 
"""
import os
import pandas as pd

root = 'KITTA_v1.0\\label_2'
dst_path = 'KITTA_tracking\\label_02'

# seq_list = reversed(os.listdir(root))  # 逆序排列
seq_list = os.listdir(root)
# print(seq_list)


for i, seq in enumerate(seq_list):
    current_seq = os.path.join(root, seq)
    file_list = os.listdir(current_seq)
    # print(file_list)
    new_seq_id = i+21
    new_seq_name = str(new_seq_id).zfill(4)

    label_name = new_seq_name+'.txt'
    print(label_name)

    # 打开label输出文件夹
    labels = pd.DataFrame(data=None, columns=['frame', 'track_id', 'type', 'truncated', 'occluded',
                          'alpha', 'xmin', 'ymin', 'xmax', 'ymax', 'dimx', 'dimy', 'dimz', 'x3D', 'y3D', 'z3D', 'r_y'])
    # print(labels)
    # 遍历原始KITTA数据集每一帧的标注
    for j, file in enumerate(file_list):
        current_file = os.path.join(current_seq, file)

        # 读取每一帧标注
        label = pd.read_csv(current_file, sep=' ', index_col=False, names=[
            'type', 'track_id', 'truncated', 'occluded', 'alpha', 'xmin', 'ymin', 'xmax', 'ymax', 'dimx', 'dimy', 'dimz', 'x3D', 'y3D', 'z3D', 'r_y'])
        # 插入一列 记录帧数
        label.insert(0, 'frame', j)

        # 对调track_id和type列
        track_id = label['track_id']
        label.drop(labels=['track_id'], axis=1, inplace=True)
        label.insert(1, 'track_id', track_id)
        # print(label)
        labels = pd.concat([labels, label], ignore_index=True)
    
    # 去掉重复的track id 把hash值转换成0 1 2 ...
    track_ids = labels['track_id'].drop_duplicates().tolist()
    track_ids = dict(enumerate(track_ids))
    # print(track_ids.values())
    labels['track_id'].replace(track_ids.values(), track_ids.keys(), inplace=True)
    # print(labels)
    labels.to_csv(os.path.join(dst_path, label_name), index=0,header=0, sep=' ')
    
    

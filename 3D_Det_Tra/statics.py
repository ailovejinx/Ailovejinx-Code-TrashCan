"""
  @ Author       : Ailovejinx
  @ Date         : 2023-03-21 10:04:52
  @ LastEditors  : Ailovejinx
  @ LastEditTime : 2023-03-28 16:49:27
  @ FilePath     : statics.py
  @ Description  : get dataset characteristics, e.g. the number of target categories, number of frames and so on.
  @ Copyright (c) 2023 by Ailovejinx, All Rights Reserved. 
"""
import os
import pandas as pd

# path = 'mix_kitti/object/training/label_2'
path = 'KITTA/training/label_2'


height_sum = 0
weight_sum = 0
length_sum = 0
classes = ['Car', 'Pedestrian', 'Cyclist', 'Van', 'Truck', 'Misc']
count = [0, 0, 0, 0, 0, 0]

for dir in os.listdir(path):
    file = os.path.join(path, dir)

    label = pd.read_csv(file, sep=' ', index_col=False, names=[
                        'type', 'truncated', 'occluded', 'alpha', 'xmin', 'ymin', 'xmax', 'ymax', 'dimx', 'dimy', 'dimz', 'x3d', ' y3d', 'z3d', 'r_y'])
    # print(label)
    # print(len(label))
    for i in range(len(label)):
        for j in range(6):
            if label.iloc[i, 0] == classes[j]:
                count[j] += 1
                height_sum += label.iloc[i, 8]
                weight_sum += label.iloc[i, 9]
                length_sum += label.iloc[i, 10]

# height_ave = height_sum/count
# weight_ave = weight_sum/count
# length_ave = length_sum/count


# print(car_count, height_sum, weight_sum, length_sum)
# print(height_ave, weight_ave, length_ave)

for i in range(6):
    print("{}: {}\n".format(classes[i], count[i]))




# Car: 
# 103098 162749.05163994047 207650.95195007295 516940.84792022384
# 1.578585924459645 2.014112319832324 5.014072512757026

# Cyclist:
# 2370 4131.880359999933 1869.138843999979 5014.660930000009
# 1.7434094345991278 0.7886661789029447 2.115890687763717

# Pedestrian: 
# 11581 24818.95607000215 13610.762399996742 5790.5
# 2.1430753881359252 1.1752665918311667 0.5

# KITTA:
# Car: 103098

# Pedestrian: 11581

# Cyclist: 2370

# Van: 3261

# Truck: 3589

# Misc: 2894
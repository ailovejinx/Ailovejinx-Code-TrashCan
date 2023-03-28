"""
  @ Author       : Ailovejinx
  @ Date         : 2023-03-28 14:58:10
  @ LastEditors  : Ailovejinx
  @ LastEditTime : 2023-03-28 16:36:00
  @ FilePath     : calib_convert.py
  @ Description  : Convert old_calib to new_calib in KITTA.
                    old_calib: only one line, P2 matrix
                    new_calib: P0-P3, R0_rect, Tr_velo_to_cam, Tr_imu_to_velo, the same as KITTI's calib format.
  @ Copyright (c) 2023 by Ailovejinx, All Rights Reserved. 
"""
import os

import pandas as pd


path = 'KITTA_v1.1/calib'

dst_path = 'kitti_calib'


file_list = os.listdir(path)
# print(file_list)

for file in file_list:
    # 读取原calib内容
    current_file = os.path.join(path, file)
    calib = open(current_file)
    line = calib.read()
    # print(line)
    
    current_file_new = os.path.join(dst_path,file)
    calib_new = open(current_file_new,'w')
    calib_new.write('P0: 0 0 0 0 0 0 0 0 0 0 0 0\n')
    calib_new.write('P1: 0 0 0 0 0 0 0 0 0 0 0 0\n')
    calib_new.write(line)
    calib_new.write('P3: 0 0 0 0 0 0 0 0 0 0 0 0\n')
    calib_new.write('R0_rect: 0 0 0 0 0 0 0 0 0\n')
    calib_new.write('Tr_velo_to_cam: 0 0 0 0 0 0 0 0 0 0 0 0\n')
    calib_new.write('Tr_imu_to_velo: 0 0 0 0 0 0 0 0 0 0 0 0\n')
    
    calib.close()
    calib_new.close()
    

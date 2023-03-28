"""
  @ Author       : Ailovejinx
  @ Date         : 2023-03-28 14:58:10
  @ LastEditors  : Ailovejinx
  @ LastEditTime : 2023-03-28 16:45:54
  @ FilePath     : gen_calib.py
  @ Description  : generate calib for tracking from raw KITTA dataset.
  @ Copyright (c) 2023 by Ailovejinx, All Rights Reserved. 
"""
import os
from shutil import copyfile

root_path = 'KITTA_tracking\\calib'

for i in range(22, 108):
    filename = str(i).zfill(4)+'.txt'
    dst_path = os.path.join(root_path, filename)
    
    copyfile(os.path.join(root_path, '0021.txt'), dst_path)
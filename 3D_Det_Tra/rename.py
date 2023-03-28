"""
  @ Author       : Ailovejinx
  @ Date         : 2023-03-28 14:09:31
  @ LastEditors  : Ailovejinx
  @ LastEditTime : 2023-03-28 16:48:05
  @ FilePath     : rename.py
  @ Description  : rename the images of each sequence from '000000.jpg'
  @ Copyright (c) 2023 by Ailovejinx, All Rights Reserved. 
"""
import os

root = 'image_02'

seq_list = list(reversed(os.listdir(root)))  # 逆序排列
# seq_list = os.listdir(root)
# print(seq_list)


for i, seq in enumerate(seq_list):
    current_seq = os.path.join(root, seq)
    file_list = list(reversed(os.listdir(current_seq)))
    # print(file_list)

    for j, file in enumerate(file_list):
        current_file = os.path.join(current_seq, file)
        # print(j, current_file)

        new_name = str(j).zfill(6)+'.jpg'
        dst_path = os.path.join(current_seq, new_name)
        # if seq=='0021':
        #     print(dst_path, current_file)
        os.rename(current_file, dst_path)
    print(seq)
        
        
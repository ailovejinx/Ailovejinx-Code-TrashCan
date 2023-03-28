"""
  @ Author       : Ailovejinx
  @ Date         : 2023-03-28 14:58:10
  @ LastEditors  : Ailovejinx
  @ LastEditTime : 2023-03-28 16:47:13
  @ FilePath     : image2video.py
  @ Description  : convert image sequence to video.
  @ Copyright (c) 2023 by Ailovejinx, All Rights Reserved. 
"""
import cv2
import numpy as np
import glob
import os

# 其它格式的图片也可以
img_array = []
for filename in glob.glob('.\image_2\*.png'):
    # print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

# avi：视频类型，mp4也可以
# cv2.VideoWriter_fourcc(*'DIVX')：编码格式
# 5：视频帧率
# size:视频中图片大小
fps = 25
out = cv2.VideoWriter('all.avi',
                      cv2.VideoWriter_fourcc(*'DIVX'),
                      fps, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

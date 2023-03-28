"""
  @ Author       : Ailovejinx
  @ Date         : 2023-03-28 14:58:10
  @ LastEditors  : Ailovejinx
  @ LastEditTime : 2023-03-28 16:45:47
  @ FilePath     : form_convert.py
  @ Description  : Generate KITTA dataset.
  @ Copyright (c) 2023 by Ailovejinx, All Rights Reserved. 
"""

import os
import shutil
# import matplotlib.image as mpimg
from PIL import Image

import pandas as pd



def gen_filename(id, extension):
    """
      @ description: Generate filename from ID and extension.
      @ param       {*} id: id of image/label/calib, e.g. '000001'
      @ param       {*} extension: .png/.jpg/.txt etc.
      @ return      {*} filename: e.g. 000001.txt
    """
    id = str(id)
    id = id.zfill(6)
    filename = id + extension
    return filename


def copyfile_calib(srcfile, dstpath, filename):
    """
      @ description: copy calib to the dstpath
      @ param       {*} srcfile: source file path
      @ param       {*} dstpath: file copy destination path
      @ param       {*} filename: copy filename
      @ return      {*} none
    """
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        if not os.path.exists(dstpath):
            # make directory
            os.makedirs(dstpath)
        shutil.copy(srcfile, os.path.join(
            dstpath, filename))          # copy file


def copyfile_label(srcfile, dstpath, filename):
    """
      @ description: copy label to the dstpath
      @ param       {*} srcfile: source file path
      @ param       {*} dstpath: file copy destination path
      @ param       {*} filename: copy filename
      @ return      {*} none
    """
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        if not os.path.exists(dstpath):
            # make directory
            os.makedirs(dstpath)
        labels = pd.read_csv(srcfile, sep=' ', index_col=False, names=[
                             'type', 'track_id', 'truncated', 'occluded', 'alpha', 'xmin', 'ymin', 'xmax', 'ymax', 'dimx', 'dimy', 'dimz', 'x3D', 'y3D', 'z3D', 'r_y'])
        labels.drop(columns='track_id', axis=1, inplace=True)
        labels.to_csv(os.path.join(dstpath, filename),
                      sep=' ', index=False, header=False, mode='wb', encoding='utf8', line_terminator='\n') # should use UNIX LF
        # shutil.copy(srcfile, os.path.join(
        #     dstpath, filename))          # copy file


def gen_data(path, extension, dataname):
    """
      @ description: generate image/label/calib. if is image, conver 32bit png to 24bit, only drop alpha channel.
      @ param       {*} path: output path
      @ param       {*} extension: .txt for calib and label, .png for image
      @ param       {*} dataname: output dir name, e.g. calib image_2 label_2
      @ return      {*} none
    """
    dirs = os.listdir(path)
    count = 0
    # for dir in dirs:
    for i in range(0, 87):
        # file_list = os.listdir(os.path.join(path, dir))
        file_list = os.listdir(os.path.join(path, dirs[i]))
        # print(path)

        for file in file_list:
        # print(file_list)
            current_file = os.path.join(path, dirs[i], file)
            # current_file = os.path.join(path, dir, file_list[i])
            # print(current_file)
            filename = gen_filename(count, extension)
            # print(filename)
            dstpath = os.path.join("KITTA_v1.1", dataname)

            if(dataname == 'image_2'):
                # for image, we should convert its bit depth from 32 to 24, drop Alpha
                # print(mpimg.imread(current_file).shape)
                if not os.path.exists(dstpath):
                    # make directory
                    os.makedirs(dstpath)

                img = Image.open(current_file)
                img_24bit = img.convert('RGB')
                img_24bit.save(os.path.join(dstpath, filename))

            elif (dataname == 'calib'):
                copyfile_calib(current_file,
                               dstpath, filename)
            else:
                copyfile_label(current_file, dstpath, filename)
            count += 1

        print('{} {} done!'.format(dataname, dirs[i]))


if __name__ == "__main__":

    dataset_path = "KITTA_v1.0"

    calib_path = dataset_path + "/calib"
    label_path = dataset_path + "/label_2"
    image_path = dataset_path + "/image_2"

    # generate calib folder
    # gen_data(calib_path, '.txt', 'calib')
    gen_data(label_path, '.txt', 'label_2')
    # gen_data(image_path, '.png', 'image_2')

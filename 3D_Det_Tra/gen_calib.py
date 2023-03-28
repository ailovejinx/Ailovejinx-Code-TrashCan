import os
from shutil import copyfile

root_path = 'KITTA_tracking\\calib'

for i in range(22, 108):
    filename = str(i).zfill(4)+'.txt'
    dst_path = os.path.join(root_path, filename)
    
    copyfile(os.path.join(root_path, '0021.txt'), dst_path)
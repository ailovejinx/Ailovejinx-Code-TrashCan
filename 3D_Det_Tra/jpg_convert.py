from PIL import Image
import os

root = 'KITTA_v1.0\\image_2'
dst_path = 'KITTA_tracking\\image_02'

# seq_list = reversed(os.listdir(root))  # 逆序排列
seq_list = os.listdir(root)
# print(seq_list)


for i, seq in enumerate(seq_list):
    current_seq = os.path.join(root, seq)
    file_list = os.listdir(current_seq)
    # print(file_list)
    new_seq_id = i+21
    new_seq_name = str(new_seq_id).zfill(4)
    for j, file in enumerate(file_list):
        current_file = os.path.join(current_seq, file)
        # print(current_file)
        
        im = Image.open(current_file)
        im = im.convert('RGB')
        name = os.path.splitext(file)[0]
        # id = str(j).zfill(6)
        jpg_name = name+'.jpg'
        # print(file, jpg_name)
        dst = os.path.join(dst_path, new_seq_name, jpg_name)
        print(dst)
        if not os.path.exists(os.path.join(dst_path, new_seq_name)):
            os.mkdir(os.path.join(dst_path, new_seq_name))
            
        im.save(dst, quality=100)
        
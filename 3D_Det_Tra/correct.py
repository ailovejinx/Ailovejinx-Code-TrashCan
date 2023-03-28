import pandas as pd
import os

path = './label_2'


dirs = os.listdir(path)

for dir in dirs:
    # print(dir)
    current_file = os.path.join(path, dir)
    labels = pd.read_csv(current_file, sep=' ', index_col=False, names=[
                             'type', 'track_id', 'truncated', 'occluded', 'alpha', 'xmin', 'ymin', 'xmax', 'ymax', 'dimx', 'dimy', 'dimz', 'x3D', 'y3D', 'z3D', 'r_y'])
    
    ids = [128264,125960]

    for i in ids: 
        id = labels['track_id'].loc[labels['track_id']==i]
        flag = len(id)

        # print(flag)
        if flag!=0:
            id = id.index[0]
            # print(id)
            labels.drop(index=id, axis=0,inplace=True)
        
    labels.to_csv(os.path.join('./label_2', dir),
                      sep=' ', index=False, header=False)
    # print(labels)
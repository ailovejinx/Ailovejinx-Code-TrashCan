import os
#定义来源文件夹
path_src = 'label_2_old'
#定义目标文件夹
path_dst = 'label_2'
#自定义格式，例如“报告-第X份”，第一个{}用于放序号，第二个{}用于放后缀

def doc_rename(path_src,path_dst):
    for i, file in enumerate(reversed(os.listdir(path_src))):
        #获取原始文件名
        doc_src = os.path.join(path_src, file)
        #重命名
        j = i+100000
        doc_name = str(j).zfill(6)+'.txt'
        print(file, doc_name)
        #确定目标路径
        doc_dst = os.path.join(path_dst, doc_name)
        os.rename(doc_src,doc_dst)

#运行函数
doc_rename(path_src,path_dst)
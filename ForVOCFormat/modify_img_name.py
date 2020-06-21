# ddy_2020_2_1_23:22        //to prevent loss of image caused by overwrite
# -*- coding:utf8 -*-
 
import os
 
class BatchRename():
 
    def __init__(self):
 
        self.path = 'JPEGImages'

    def jpg_to_jpeg(self):
            filelist = os.listdir(self.path)
            total_num = len(filelist)
            for item in filelist:
                if item.endswith('.jpg'):
                    src = os.path.join(os.path.abspath(self.path), item)
                    dst = os.path.join(os.path.abspath(self.path), 'nocrack'+str(i+1)+ '.jpeg')
                    try:
                        os.rename(src, dst)
                        i = i + 1
                    except:
                        continue
                elif item.endswith('.jpeg'):
                    src = os.path.join(os.path.abspath(self.path), item)
                    dst = os.path.join(os.path.abspath(self.path), 'nocrack'+str(i+1)+ '.jpeg')
                    try:
                        os.rename(src, dst)
                        i = i + 1
                    except:
                        continue

 

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'nocrack'+str(i+1)+ '.jpeg')
                try:
                    os.rename(src, dst)
                    i = i + 1
                except:
                    continue
            elif item.endswith('.jpeg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'nocrack'+str(i+1)+ '.jpeg')
                try:
                    os.rename(src, dst)
                    i = i + 1
                except:
                    continue

    # ddy_2020_2_1_23:22        //to prevent loss of image caused by overwrite
    def prerename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'unnamedimg'+str(i+1)+ '.jpeg')
                try:
                    os.rename(src, dst)
                    i = i + 1
                except:
                    continue
            elif item.endswith('.jpeg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'unnamedimg'+str(i+1)+ '.jpeg')
                try:
                    os.rename(src, dst)
                    i = i + 1
                except:
                    continue
 
if __name__ == '__main__':
    demo = BatchRename()
    demo.prerename()
    demo.rename()

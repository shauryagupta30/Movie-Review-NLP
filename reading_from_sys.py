import os
files_pos = os.listdir(r'C:/Users/dell/Desktop/train_pos')
files_neg = os.listdir(r'C:/Users/dell/Desktop/train_neg')
files_pos = [open(r'C:/Users/dell/Desktop/train_pos/'+f, 'r',encoding="utf8").read() for f in files_pos]

files_neg = [open(r'C:/Users/dell/Desktop/train_neg/'+f, 'r',encoding="utf8").read() for f in files_neg]

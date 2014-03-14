#coding:utf-8
import os
'''
一个批量修改文件名字的小脚本
'''

def RenameFile(TheFile,search_str,to_name):
    le = len(search_str)
    for the_file in os.listdir(TheFile):
        if the_file.find(search_str) != -1:
            print the_file
            key = the_file.find(search_str) 
            if key == 0:
                replace_name = to_name + the_file[le:]
            else:
                replace_name = the_file[0:key] + to_name + the_file[key+le:]
            os.rename(the_file,replace_name)

if __name__ == '__main__':
     RenameFile('.','zzz','a') 

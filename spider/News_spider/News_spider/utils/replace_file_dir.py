# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 10:27
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : replace_file_dir.py(遍历文件，并替换)
import os

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

# list = GetFileList('', [])
# for e in list:
#     print(e)

# 替换文件夹的名字，包括文件夹的字符串含有子字符串
def replaceDirName(rootDir, oldStr, newStr):
    for dirpath, dirNames, fileNames in os.walk(rootDir, topdown=False):
        for dirName in dirNames:
            if oldStr in dirName:
                dirNameOld = os.path.join(dirpath, dirName)
                dirNameNew = os.path.join(dirpath, dirName.replace(oldStr, newStr))
                # print(dirNameOld + ' --> ' + dirNameNew)
                os.rename(dirNameOld, dirNameNew)

    # 替换文件名
def replaceFileName(rootDir, oldStr, newStr):
    # print('replaceFileName ==== > ')
    for dirpath, dirNames, fileNames in os.walk(rootDir):
        for fileName in fileNames:
            if oldStr in fileName:
                fileNameOld = os.path.join(dirpath, fileName)
                fileNameNew = os.path.join(dirpath, fileName.replace(oldStr, newStr))
                # print(fileNameOld + ' --> ' + fileName)
                os.renames(fileNameOld, fileNameNew)


    # 替换文件中的内容
def replaceFileContent(rootDir, oldStr, newStr):
    for dirpath, dirNames, fileNames in os.walk(rootDir):
        for fileName in fileNames:
            fileObj = os.path.join(dirpath, fileName)
            f = open(fileObj, 'r+',encoding="utf-8")
            all_the_lines = f.readlines()
            f.seek(0)
            f.truncate()
            for line in all_the_lines:
                line = line.replace(oldStr, newStr)
                f.write(line.replace('jk',newStr))
            f.close()
            # 执行流


if __name__ == '__main__':
    rootDir = r"D:\Django_ZM\test\test"
    oldStr = "JK"
    newStr = "SK"
    try:

        # 替换文件中的内容
        replaceFileContent(rootDir, oldStr, newStr)
        pass
    except Exception as e:
        # print('e1 ===> ',e)
        pass
    try:
        # 替换文件名
        replaceFileName(rootDir, oldStr, newStr)
        pass
    except Exception as e:
        # print('e2 === ',e)
        pass

    try:
        # 替换文件夹
        replaceDirName(rootDir, oldStr, newStr)
        pass
    except Exception as e:
        # print('e3  ==== ',e)
        pass


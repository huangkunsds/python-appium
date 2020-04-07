#coding=utf-8
import os
def getSpecialPath(dirName, topPathName = 'up366_appUI_stu'):
    u'''根据目标目录名和给定顶层目录名，在此范围内返回目标目录'''
    u'''目标目录名要唯一'''
        
    abPath = u'' #目标目录路径，默认为空
    cp = u'.\\' #当前脚本的上层目录
    while len(dirName) > 1:
        p = os.path.abspath(cp) #当前脚本的绝对路径
        yid = os.walk(p)
        for rootDir, pathList, fileList in yid:  
            for path in pathList:
                #print 'path ' + os.path.join(rootDir, path)
                if dirName == path or dirName == path.lower():
                    abPath = os.path.join(rootDir, path)
                    return (abPath + '\\')
                
        cp = cp + u'..\\' 
        if topPathName == p[p.rfind('\\')+1:]:
            #msg = u"Not find special path: '%s', please confirm the path name is correct." % dirName
            abPath = u'not found the dir'
            return False
        
        
def getSpecialFile(fileName, topPathName= 'untitled'):
    u'''根据目标文件名和给定顶层目录名，在此范围内返回包含目标文件的绝对路径'''
    u'''文件名要唯一，可以是带部分路径的'''
    abPath = u''
    cp = u'.\\' #当前脚本的上层目录
    while len(fileName) > 1:
        p = os.path.abspath(cp) #当前脚本的绝对路径
        yid = os.walk(p)
        for rootDir, pathList, fileList in yid:
            for fname in fileList:
                #文件名不包含路径：
                if '\\' in fileName:
                    fp = os.path.join(rootDir, fname)
                    if fileName in fp or fileName in fp.lower():
                        abPath = os.path.join(rootDir, fp)
                        return abPath
                #文件名包含路径：
                else:
                    if fileName == fname or fileName == fname.lower():
                        abPath = os.path.join(rootDir, fname)
                        return abPath
        
        cp = cp + u'..\\' 
        if topPathName == p[p.rfind('\\')+1:]:
            #msg = u"Not find special file: '%s', please confirm the file name is correct." % fileName
            abPath = u'not found the file'
            return False           
                    
if __name__ == u'__main__':
    tp = getSpecialPath(u'data')
    print(u'返回的目录路径:\n', tp)
    tf = getSpecialFile('name.yaml')
    print(u'返回的文件路径:\n', tf)
    
# -*- coding: utf-8 -*-

'''
Given an absolute path for a file (Unix-style), simplify it. 

给定一个文件的绝对路径（unix系统），将其简化。

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

在unix文件系统中，'.' 表示当前目录，因此可以被忽略。'..' 表示上一个目录，因此需要取消掉最后一层目录。

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

边界示例：
1、"/../" 应该返回 "/"
2、"/home//foo/" 应该返回 "/home/foo"
'''
import re
def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    先将斜线之间的目录按顺序提取出来，然后从左到右进行 . 和 .. 的分析。
    """
    # 将多个斜线换成1个
    pattern = re.compile(r'/{2,}')
    path = re.sub(pattern, '/', path)
    
    # 分割
    splits = path.split('/')
    results = []
    for split in splits:
        if (split == '..' and len(results) == 1) or (split == '.'):
            continue
        if split == '..':
            results = results[:-1]
        else:
            results.append(split)
    result = '/'.join(results)
    if result == '': # 为空时返回一个斜杠
        result = '/'
    elif len(result) > 1 and result[-1] == '/': # 去掉最后一个斜杠
        result = result[:-1]
    return result

if '__main__' == __name__:
    path = "/"
    print(simplifyPath(path))
                
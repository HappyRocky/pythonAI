# -*- coding: utf-8 -*-

"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
You may assume the default revision number for each level of a version number to be 0. 
For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. 
Its third and fourth level revision number are both 0.

Note:
Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
Version strings do not start or end with dots, and they will not be two consecutive dots.

比较两个版本号 version1 和 version2。
如果 version1 > version2 则返回1；如果 version1 < version2 则返回-1；否则返回0.
可以假设版本号字符串是非空的，且只包含数字和'.'字符。
. 字符不代表一个小数点，而是用来区分数字序列。
比如，2.5 表示第二个一阶版本的第5个二阶版本。
可以假设每阶版本号的默认数字是0.
比如，版本号 3.4 的三阶和四阶版本号都是0.

备注：
版本号字符串的每阶版本数字可能以0开头。
版本号字符串不会以 . 开头或结尾，并且不会有连续的两个.。

Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

Example 4:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”

Example 5:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
 
"""

def compareVersion(version1: str, version2: str) -> int:
    """
    按照顺序比较每阶数字，高阶数字一旦比较出了大小，便不用继续比较低阶的。
    """
    # 切割出各阶版本数字
    v1_list = [int(x) for x in version1.split('.')]
    v2_list = [int(x) for x in version2.split('.')]
    # 两个版本号补齐，短的补0
    if len(v1_list) < len(v2_list):
        v1_list += [0] * (len(v2_list) - len(v1_list))
    elif len(v1_list) > len(v2_list):
        v2_list += [0] * (len(v1_list) - len(v2_list))
    # 比较大小
    for i in range(len(v1_list)):
        if v1_list[i] > v2_list[i]:
            return 1
        elif v1_list[i] < v2_list[i]:
            return -1
    return 0
if '__main__' == __name__:
    version1 = "01"
    version2 = "1"
    print(compareVersion(version1, version2))
# -*- coding: utf-8 -*-

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

给定一个字符串，只包含数字，返回所有可能的有效IP地址组合。

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

def restoreIpAddresses(s: str) -> list:
    """
    深度优先遍历，回溯法
    规则：IP地址分为4部分，每部分不超过255，每部分最高位不能是0，除非这部分就是0本身。
    """
    def fun(cur_list, remain_str, result_list):
        """
        cur_list: 当前的IP划分结果
        remain_str: 剩余需要划分的字符串 
        result_list: 存放所有有效的结果
        """
        # 递归结束条件
        if len(cur_list) == 4:
            if not remain_str:
                result_list.append('.'.join(cur_list))
            return
        # 继续划分
        if len(remain_str) >= 1:
            fun(cur_list + [remain_str[0]], remain_str[1:], result_list)
            if remain_str[0] != '0':
                if len(remain_str) >= 2:
                    fun(cur_list + [remain_str[:2]], remain_str[2:], result_list)
                if len(remain_str) >= 3 and int(remain_str[:3]) <= 255:
                    fun(cur_list + [remain_str[:3]], remain_str[3:], result_list)
            
    result_list = []
    fun([], s, result_list)
    return result_list

if '__main__' == __name__:
    s = "010010"
    print(restoreIpAddresses(s))
        
        
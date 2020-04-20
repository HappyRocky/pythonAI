#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CREATED: 2020/1/10
AUTHOR: gongyanshang1
DESCRIPTION: 此脚本为并行执行的工具，传入要并行执行的脚本名和补数起止日期，自动对日期进行分组和多线程执行
"""
import datetime
import subprocess
import sys

def get_date_list(start_date, end_date):
    """
    生成从起始日期到结束日期的日期列表
    :param start_date:起始日期
    :param end_date:结束如期
    :return: list
    """
    # 获取起止日期
    if start_date is not None:
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    if end_date is None:
        end = datetime.datetime.now()
    else:
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    # 将每一天加入到list中
    result_list = []
    day = datetime.timedelta(days=1)
    for i in range((end - start).days + 1):
        result_list.append((start + day * i).strftime("%Y-%m-%d"))
    return result_list


def parallel_run(file_name, date_list):
    """
    批量执行补数脚本
    :param file_name:补数脚本
    :param date_list:日期列表
    :return: list，存放失败的命令
    """
    sub_list = []  # 多线程列表
    sub_dict = dict()  # <subprocess, command>
    for d in date_list:  # 每个日期创建一个线程
        command = 'nohup python3 {} {}'.format(file_name, d)  # 补数命令
        child = subprocess.Popen(command, shell=True)
        sub_dict[child] = command
        print(command)
        sub_list.append(child)

    # 等待所有进程完毕
    for sub in sub_list:
        sub.wait()

    # 查找失败任务
    fail_list = []
    for child, command in sub_dict.items():
        if child.returncode != 0:
            fail_list.append(command)
    return fail_list

def group_run(file_name, date_list, period=31):
    """
    分组批量执行补数脚本
    :param file_name:补数脚本
    :param date_list:日期列表
    :param period: 每次最多开的线程数
    :return:
    """
    # 将日期列表按照period分组
    period_list = [date_list[0: period]]
    i = period
    while i < len(date_list):
        period_list.append(date_list[i: i + period])
        i += period

    # 将每个分组依次进行多线程执行
    fail_list = []
    for i in range(len(period_list)):
        print('并行执行第{}/{}批任务:'.format(i + 1, len(period_list)))
        fail_list.extend(parallel_run(file_name, period_list[i]))
    if fail_list:
        print('失败的命令如下:')
        for c in fail_list:
            print(c)
    else:
        print('命令全部成功')


if '__main__' == __name__:
    file_name = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    group_run(file_name, get_date_list(start_date, end_date))

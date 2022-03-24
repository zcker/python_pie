#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022-3-24 下午 03:18
# Author:ZhangChengkai
# @File    : marketA_account_for_GDP.py
# 2015年任泽平大佬预测2015年牛市顶点的计算方法，通过股市总市值和GDP比值来判断指数的高低，
# 比值介于75%~90%适合投资股市，超过120%则代表要避开股市风险

import requests
import re
import datetime


def sh_url():
    """
    上海证券交易所
    :return:
    """
    heards = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    response = requests.get('http://www.sse.com.cn/', headers=heards)
    sh = re.findall("home_sjtj.mkt_value = '(.*?)'", response.text)
    sh_number = sh.pop(0)
    sh_number = float(sh_number)
    return sh_number


def sz_url():
    """
    深交所
    :return:
    """
    response2 = requests.get(
        'http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1803_after&loading=first&random=0.9432337715587713')
    zongshizhi = re.findall('zbmc":"股票总市值（亿元）","brsz":"(.*?)"', response2.text)
    number = zongshizhi.pop(0)
    number = number.replace(',', '')
    number = float(number)
    return number


def sum_sh_sz(sh=sh_url(), sz=sz_url()):
    A = (sh + sz) / 1143669.7 * 100
    return A


def getYesterday():
    """
    昨日
    :return:
    """
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


def write(sum=sum_sh_sz(), data=getYesterday()):
    sum = str(sum)
    data = str(data)
    filename = 'GDP占比.txt'
    with open(filename, 'a') as file_object:
        file_object.write(sum + " ")
        file_object.write(data)
        file_object.write('\n')

if __name__ == '__main__':
    write()

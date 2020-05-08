#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuhz
@file: RegClass.py
@time: 2020/5/8 11:26
"""

import re

# 封装正则类
# 类初始化时接受一个字符串的参数
class Regular(object):
	def __init__(self, s):
		self.str = s
	# 方法能够匹配出所有的数字
	def get_numbers(self):
		num_pattern = re.compile('\d')
		num_list = re.findall(num_pattern, self.str)
		return num_list
	# 方法能够匹配出所有的邮箱
	def get_emails(self):
		mail_pattern = re.compile('\w*?@.*?\..{2,3}?')
		mail_list = re.findall(mail_pattern, self.str)
		return mail_list
	# 方法可以匹配出所有的ip
	def get_ips(self):
		ips_pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
		ips_list = re.findall(ips_pattern, self.str)
		return ips_list
	# 方法能够匹配出所有的电话号码,电话包含座机和移动电话，座机要考虑区号3位或4位，号码要考虑7位或8位
	def get_phone_numbers(self):
		phone_pattern = re.compile('\d{3,4}-\d{7,8}|\d{11}')
		phone_list = re.findall(phone_pattern, self.str)
		return phone_list
	# 方法能够匹配出所有的url，url可以以http开头、https开头、ftp开头
	def get_urls(self):
		urls_pattern = re.compile('http.+?\.\w{2,4}/|https.+?\.\w{2,4}/|ftp.+?\.\w{2,4}/')
		urls_list = re.findall(urls_pattern, self.str)
		return urls_list


my_str = 'Email: aBc_123@mail.cn; Page1: http://www.jianshu.com/; IP: 126.14.1.127; Phone: 010-1007230/0734-77884235/18089804653; Page2: https://www.cnblogs.com/'
my_re = Regular(my_str)
print(my_re.get_numbers())
print(my_re.get_emails())
print(my_re.get_ips())
print(my_re.get_phone_numbers())
print(my_re.get_urls())

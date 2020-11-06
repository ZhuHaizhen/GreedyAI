#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuhz
@file: SortClass.py
@time: 2020/5/8 14:06
"""

# 排序类的封装
class SortUtils(object):
	"""
	要求：有一个sort方法，方法接收两个参数，一个参数是列表，另外一个参数是排序方法
	例如：当传入bubble时，则调用冒泡排序的方法进行排序，并打印出每一步数字挪动的过程
		当传入quick时，则调用快速排序的方法进行排序，并打印出每一步数字挪动的过程
	外部不可以直接访问具体排序方法，只能调用sort方法
	"""
	def sort(self, method):
		if method == 'bubble':
			def sort_inner(l):
				for i in range(len(l)-1):
					for j in range(len(l)-1-i):
						if l[j] > l[j+1]:
							l[j], l[j+1] = l[j+1], l[j]
					# print(l)
				return l
		if method == 'quick':
			def sort_inner(l):
				if l == []:
					return []
				else:
					pivot = l[0]
					left = sort_inner([m for m in l[1:] if m < pivot])
					right = sort_inner([n for n in l[1:] if n >= pivot])
					# print(left + [pivot] + right)
				return left + [pivot] + right
		return sort_inner

my_list = [1, 5, 3, 7, 9, 14, 2, 30]
my_sort = SortUtils()
print(my_sort.sort('bubble')(my_list))
print(my_sort.sort('quick')(my_list))

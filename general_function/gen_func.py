#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
一些通用函数
'''

import difflib

def GetEditDistance(str1, str2):
	leven_cost = 0
	s = difflib.SequenceMatcher(None, str1, str2)  #SequenceMatcher是构造函数，主要创建任何类型序列的比较对象
	for tag, i1, i2, j1, j2 in s.get_opcodes():
		#print('{:7} a[{}: {}] --> b[{}: {}] {} --> {}'.format(tag, i1, i2, j1, j2, str1[i1: i2], str2[j1: j2]))
		'''get_opcodes函数每执行一次返回5个元素的元组，元组描述了从a序列变成b序列所经历的步骤。5个元素的元组表示为(tag, i1, i2, j1, j2)，其中tag表示动作，
		i1,i2分别表示序列a的开始和结束位置，j1，j2表示序列b的开始和结束位置。'''
		if tag == 'replace':            #a[i1:i2] should be replaced by b[j1:j2]
			leven_cost += max(i2-i1, j2-j1)
		elif tag == 'insert':           #b[j1:j2] should be inserted at a[i1:i1].Note that i1==i2 in this case.
			leven_cost += (j2-j1)
		elif tag == 'delete':           #a[i1:i2] should be deleted. Note that j1==j2 in this case.
			leven_cost += (i2-i1)
	return leven_cost
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
获取符号字典列表的程序
'''


def GetSymbolList(datapath):
	'''
	加载拼音符号列表，用于标记符号
	返回一个列表list类型变量
	'''
	if(datapath != ''):
		if(datapath[-1]!='/' or datapath[-1]!='\\'):
			datapath = datapath + '/'
	
	txt_obj=open(datapath + 'dict.txt','r',encoding='UTF-8') # 打开文件并读入   dict.txt是pny2hanzi字典
	txt_text=txt_obj.read()        #read()读取整个文件
	txt_lines=txt_text.split('\n') # 文本分割    #split返回字符串列表    分隔每个拼音
	list_symbol=[] # 初始化符号列表
	for i in txt_lines:
		if(i!=''):
			txt_l=i.split('\t')						#分隔拼音和多音字
			list_symbol.append(txt_l[0])            #提取拼音
	txt_obj.close()
	list_symbol.append('_')
	#SymbolNum = len(list_symbol)
	return list_symbol
	

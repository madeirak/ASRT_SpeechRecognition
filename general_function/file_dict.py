#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
获取符号字典列表的程序
'''
import platform as plat


def GetSymbolList(datapath):
	'''
	加载拼音符号列表，用于标记符号
	返回一个列表list类型变量
	'''

	datapath_ = datapath.strip('dataset\\')

	system_type = plat.system()  # 由于不同的系统的文件路径表示不一样，需要进行判断
	if (system_type == 'Windows'):
		datapath_+='\\'
	elif (system_type == 'Linux'):
		datapath_ += '/'
	else:
		print('*[Message] Unknown System\n')
		datapath_ += '/'


	txt_obj=open(datapath_ + 'dict.txt','r',encoding='UTF-8') # 打开文件并读入   dict.txt是pny2hanzi字典
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


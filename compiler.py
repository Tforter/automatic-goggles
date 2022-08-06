import os.path
import re
from enum import Enum

class tokentype(Enum):
	VARIABLE_NAME = 0
	ASSIGNMENT_OP = 1
	ADD_OP = 2
	SUB_OP = 3
	MUL_OP = 4
	DIV_OP = 5
	INTEGER_VALUE = 6
	BOOLEAN_VALUE = 7
	STRING_VALUE = 8

class token:
	def __init__(self, type, value):
		self.type = type
		self.value = value
	def __str__(self):
		return '{' + self.type.name + ', ' + str(self.value) + '}'

def compileTK(file):
	if not os.path.exists(file):
		print('File not found \'' + file + '\'')
		quit()
	
	text = open(file, 'r').read()
	text = text.split(';')
	tokens = []
	
	for ele in text:
		line = re.split(r'\s|\n', ele)
		line = [x for x in line if x]
		toks = []
		print(ele)
		for i in range(0, len(line)):
			current = line[i]
			print(current)
			# assignment
			if current == '=' or current == '+=' or current == '-=' or current == '*=' or current == '/=':
				toks.append(token(tokentype.ASSIGNMENT_OP, current))
				print('found assignment')
				continue
			
			# operation
			if current == '+':
				toks.append(token(tokentype.ADD_OP, current))
				print('add op')
				continue
			if current == '-':
				toks.append(token(tokentype.SUB_OP, current))
				print('sub op')
				continue
			if current == '/':
				toks.append(token(tokentype.DIV_OP, current))
				print('div op')
				continue
			if current == '*':
				toks.append(token(tokentype.MUL_OP, current))
				print('mul op')
				continue
			
			# string
			if current.startswith('"') and current.endswith('"'):
				toks.append(token(tokentype.STRING_VALUE, current))
				print('found string')
				continue
			
			# boolean
			if current.lower() == 'true':
				toks.append(token(tokentype.BOOLEAN_VALUE, True))
				print('found boolean true')
				continue
			if current.lower() == 'false':
				toks.append(token(tokentype.BOOLEAN_VALUE, False))
				print('found boolean false')
				continue
			
			if (ord(current[0]) >= 65 and ord(current[0]) <= 90) or (ord(current[0]) >= 97 and ord(current[0]) <= 122):
				toks.append(token(tokentype.VARIABLE_NAME, current))
				print('variable name')
				continue
			
			# integer
			try:
				toks.append(token(tokentype.INTEGER_VALUE, int(current)))
				print('found integer')
				continue
			except Exception:
				pass
		tokens.append(toks)
	
	i = 0
	for t1 in tokens:
		print('token ' + str(i))
		for t2 in t1:
			print(str(t2))
		i = i + 1
	

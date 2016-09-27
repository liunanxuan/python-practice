#-*- coding:utf-8 -*-
import string
import random
def get_activation_code(count,length):
	#count生成多少个激活码
	#length激活码的长度
	results = set()
	source = list(string.ascii_uppercase)
	for number in range(0,10):
		source.append(str(number))
	while len(results) < count:
		key = ''
		for x in range(0,length):
			key +=random.choice(source)
		if key in results:
			pass
		else:
			results.add(key)
	for result in results:
		print result

if __name__ == "__main__":
	#count = 200
	#for test code
	count  = 20
	length = 16
	get_activation_code(count, length)

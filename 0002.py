#-*- coding:utf-8 -*-
import string
import random
import MySQLdb
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
	#test result
	#for result in results:
	#	print result
	if len(results) > 0:
		return results
	else:
		return None


if __name__ == "__main__":
	#count = 200
	#for test code
	count  = 20
	length = 16
	values = set()
	values = get_activation_code(count, length)
	conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd = 'root',charset='utf8',db='liunx')
	cursor = conn.cursor()
	#for x in range(length):
	for value in values:
		strsql = "insert into activationcode(activation) values ('%s')" % value
		print strsql
		try: 
			cursor.execute(strsql)
			conn.commit()
		except Exception as e:
			print e
			conn.rollback()
	conn.close()
	cursor.close()

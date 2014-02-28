#coding=utf-8

list_in=raw_input("please input the math:")

k=0
for i in list_in:
	k+=1
	if int(i)==0:	
		print k
		one=""
		for j in range(0,k-1):	
			one= one + list_in[j]
		print u"'0'前面的数为：%s" %one
		
		two=""
		for j in range(k,len(list_in)):
			two=str(two)+list_in[j]
		print u"'0'后面的数为：%s" %two
		break
def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a+b

def sub(a,b):
	print "SUBING %d - %d" %(a,b)
	return a-b

def mul(a,b):
	print "MULING %d * %d" %(a,b)
	return a*b

def div(a,b):
	print "DIVING %d / %d" %(a,b)
	return a/b

def div_diy(a,b):
	print "DIVING %d / %d" %(a,b)
	return a/b,a%b

print "Let's do some math with just functions!"

age=add(30,5)
height=sub(78,4)
weight=mul(90,2)
iq=div(80,2)

print "Age:%d, Height:%d, Weight:%d,IQ: %d"%(age,height,weight,iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what=add(age,sub(height,mul(weight,div(iq,2))))

print "That becomes: ",what,"Can you do it by hand"

arg1,arg2=div_diy(80,3)
print arg1,arg2
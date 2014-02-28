
def wh_loop(j):
	i = 0
	numbers=[]

	while i < j:	
		print "At the top i is %d."% i
		numbers.append(i)

		i+=1
		print "Numbers now: ",numbers
		print "At the bottom i is %d" %i
	return numbers

print "Please input a number:"
j=raw_input("> ")
numbers=wh_loop(int(j))
print numbers
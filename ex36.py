#coding=utf-8
import random

def ds():
	counts=random.randint(1,6)
	return counts

def lucky(times):
	if times <= 8:
		print "your lucky is best."
	elif times <= 10:
		print "your lucky is better."
	elif times <= 12:
		print "your luck is good."
	else:
		print "your lucky is bad."


def start():
	print "This game is about dice."
	print "The dice's number is 1 to 6."
	print "Now let's begin,please hit ENTER"
	score = 0
	times = 0
	list_ds=[]

	while score <= 40:
		raw_input("> ")
		ds1=ds()
		times+=1
		print "Your number is %d." % ds1
		list_ds.append(ds1)
		score=score+ds1
		print "This is your %d times,your score is %d." % (times,score)
		print "please hit ENTER to contiune."

	print u"您扔了%d次骰子，使您的分数超过40分." % times,list_ds
	lucky(times)

start()
#coding=utf-8

from random import randint

class PlayerRu:
	'''定义玩家游戏规则'''
	def __init__(self,player):
		self.player=player

	def runtest1(self):
		'''先判断状态，为1再摇点数，计算最后分数'''
		if self.player[2]!=0:
			print ("ENTER by %s >>")%self.player[0],raw_input()
			points=playpoint()
			self.player[1]+=points
			print "%s get %d ponits,now your points is %d"%(self.player[0],points,self.player[1])
		else:
			exit(1)


	def countplay(self):
		'''根据分数做不同操作'''
		if self.player[1]>=100:
			print "Congratulation %s .You WIN!"%self.player[0]
			exit(0)

		elif self.player[1]%10==4:
			print "Bad lucky!You will be frozen"
			self.player[2]=0

		elif self.player[1]%10==8:
			print "Good lucky!You will get 2 points"
			self.player[1]+=2

		elif self.player[1]%10==3:
			print "Good lucky!You will lost 2 points"
			self.player[1]-=2

		elif self.player[1]==55:
			print "You got lucky points,Reward 5 ponits"
			self.player[1]+=5

		else:
			print "There is nothing,Continue the game"
	def main(self):
		'''主函数，玩家数据处理'''
		self.runtest1()
		self.countplay()





		
def playpoint():
	'''摇点数'''
	curr_point=randint(1,6)
	return curr_point
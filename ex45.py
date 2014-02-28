#coding=utf-8
#miyavi0000a


from sys import exit
from ex45_class import PlayerRu

class Game(object):
	def __init__(self):
		pass

	def start(self):
		'''输入玩家名字，支持多人在线.'''
		print "The Game is Monopoly"
		input_name=raw_input("please Enter the names of all players,\nand Middle name to use ',':")
		print 
		self.names=input_name.split(',')
		table=[]
		for name in self.names:
			table.append(self.playerlist(name))
		self.table=table

	def playerlist(self,name):
		'''构造玩家数据表['name','count','status']'''
		player=[0,0,1]
		player[0]=name
		return player


	def played(self):
		'''循环执行游戏'''
		while 1:
			for i in range(len(self.names)):
				player=self.table[i]
				if player[2]:
					run=PlayerRu(player)
					run.main()
				else:
					print '%s is freeze'%player[0]
					player[2]=1
				

	def main(self):
		'''大富翁游戏'''
		self.start()
		self.played()


if __name__=="__main__":
	'''主体'''
	start=Game()
	start.main()
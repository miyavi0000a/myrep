#coding=utf-8

class Fruit:	
	price = 0	
	__a = 22	
	
	def __init__(self):		
		self.__color = "red"		
		self.__price = 11

class Apple(Fruit):             # Apple继承了Fruit	
	__b = 10	
	c = 33	

if __name__ == "__main__":    
	apple = Apple() 
	print apple.__dict__
	print Apple.__dict__ 
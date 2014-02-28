class Song():

	def __init__(self,lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def showClassName(self):
		print self.__class__.__name__

	def showClassDoc(self):
		print self.__class__.__doc__

new_year=Song(["So I say come on",
				"Open your eyes",
				"And see what's outside",
				"there's nothing to fear",
				"It's a new year"])

everything_in_the_world=Song(["How many times you asked yourself before",
							"What's the point, wasting time",
							"But how many times you stand up for yourself",
							"Make a point, you have a reason",
							"You know, it's not fair"])

new_year.sing_me_a_song()
new_year.showClassName()

everything_in_the_world.sing_me_a_song()
everything_in_the_world.showClassDoc()
#coding=utf-8

import random
from urllib import urlopen
import sys

#定义 WORD_URL,WORDS，PHRAESE
WORD_URL="http://learncodethehardway.org/words.txt"
WORDS=[]

PHRASES ={
	"class ###(###):":
	"Make a class named ### that is-a ###.",
	"class ###(object):\n\tdef __init__(self,***)":
	"class ### has-a __init__ that takes self and *** parameters.",
	"class ###(object):\n\tdef ***(self.@@@)":
	"class ### has-a function named *** that takes self and @@@ parameters",
	"***=###()":
	"Set *** to an instance of class ###.",
	"***.***(@@@)":
	"From *** get the *** function,and call it with parameters self,@@@.",
	"***.***='***'":
	"Form *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
# 定义PHRASE_FIRST为假
PHRASE_FIRST = False

#当命令行传入参数为2个，并且第二个参数为‘english’时 PHRASR_FIRST为真
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST=True

# load up the words from the website
# 从网站加载每行值添加包列表WORDS中
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())


def convert(snippet,phrase):
	# 从WORDS列表随机选取
	class_names = [w.capitalize() for w in 
				random.sample(WORDS,snippet.count("###"))]
	
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0,snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS,param_count)))

	for sentence in snippet,phrase:
		result = sentence[:]

		# fake class names:
		for word in class_names:
			result = result.replace("###",word,1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word ,1)

		#fake parameter lists
		for word in param_names:
			result = result.replace("@@@",word,1)

		results.append(result)

	return results	

try:
    while True:
    	#定义 列表snippets 为字典PHRASES的关键字
        snippets = PHRASES.keys()
        #打乱列表snippets顺序
        random.shuffle(snippets)

      	# 轮询列表snippets
        for snippet in snippets:
        # 将字典 PHRASES关键字对应值赋予列表phrase
            phrase = PHRASES[snippet]
            # 调用函数 convert,参数为：关键字，值。
            question, answer = convert(snippet, phrase)
            # 如果 PHRASE_FIRST为真，关键字与值互换。
            if PHRASE_FIRST:
                question, answer = answer, question


            print question


            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"
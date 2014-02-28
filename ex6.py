#coding=utf-8
# 变量X赋值为字符串
x = "There are %d types." % 10
# 变量binary赋值为字符串
binary="binary"
# 变量do_not赋值为字符串
do_not="don't"
# 变量y赋值为字符串并包含变量binary,do_not
y="Those who know %s and those who %s." % (binary,do_not)

#打印变量x
print x
#打印变量y
print y

print "I said: %r." % x
print "I also said: '%s'."% y

hilarious= False
joke_evaluation="Isn't that joke so funny ?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

# 打印 字符串w 串联 字符串e
print w+e
# coding=utf-8
my_name="miyavi_胡"
my_age=998 # just a lie
my_weight=65 # kilogram
my_height=175 # cm
my_eyes='Yellow'
my_teeth='White'
my_hair='black'
my_rou=round(1.7522)
my_ran=range(100)

print "Let's talk about %s." %my_name
print "He's %d kilogram heavy." %my_weight
print "He's %d cm tall." %my_height
print "Actually that's not heavy."
print "He's got %s eyes and %s hair." %(my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth
print "There are %f and %s." %(my_rou,my_ran)

# this line is tricky,try to get it exactly right
print "If I add %d, %d, and %d I get %d."%(
	my_age,my_height,my_weight,my_age+my_height+my_weight)
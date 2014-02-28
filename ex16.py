from sys import argv

script, filename=argv

print "We're going to erase %r." % filename
print "If you don't want that ,hit CTRL-C (^C)."
print "If you do want that, hit ENTER"

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

#print "Truncating the file. Goodbye"
#target.truncate()

print "Now I'm going to ask you for the lines."

target.write(raw_input("line 1: ")+"\n")
target.write(raw_input("line 2: ")+"\n")
target.write(raw_input("line 3: ")+"\n")

print "I'm going to write these to the file"
print "And finally, we close it."
target.close()
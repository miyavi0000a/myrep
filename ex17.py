from sys import argv
from os.path import exists

script, from_file, to_file=argv

print "Copying from %s to %s" %(from_file,to_file)
print "Ready, hit ENTER to continue, CTRL-C to abort"
raw_input()

out_file=open(to_file,'w')
out_file.write(open(from_file).read())

print "Alright,all done"

out_file.close()
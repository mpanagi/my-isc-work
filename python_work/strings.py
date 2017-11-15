# splitting a string to loop it's words:
'''
s = "I love to write Python"

split_s = s.split()
for word in split_s:
	if word.find("i") > -1: 
		print "I found 'i' in: '{0}'".format(word)
'''
# Useful aspects of strings:
'''
something = "Completely Different"

#print dir(something)

print something.count("t")
print something.find("plete")

print something.split("e")

thing2 = something.replace("Different", "Silly")

print thing2

# something[0] = "B" This does not work because strings are immutable. They cannot be changed
'''



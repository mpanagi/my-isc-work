# Never ending while loop

#while 1:
#    x = 1
	# Escape using ctrl + C
#while 5:
#    pass


gases = ['He', 'Ne', 'Ar', 'Kr']
count = 0
while count < 4:
    item = gases[count]
    print item, gases.index(item)
    count += 1


# if, elif and else:

x=0
if x == 2:
    print x
elif x == 1:
    print 1
else:	#use else to catch the other possibilities (other than 1 and 2)
    print "horray"

x = [1, 1, 4, 5, 1, 1]
while 1 in x:
    print x
    x.remove(1)

#or you can use set:

s = set(x)
s


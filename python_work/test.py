# Never ending while loop

#while 1:
#    x = 1
	# Escape using ctrl + C
#while 5:
#    pass


mylist = [23, "hi", 2.4e-10]
count = 0
while count < 3:
    item = mylist[count]
    print item, mylist.index(item)
    count += 1

# if, elif and else:

x=0
if x == 2:
    print x
elif x == 1:
    print 1
else:	#use else to catch the other possibilities (other than 1 and 2)
    print "horray"


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

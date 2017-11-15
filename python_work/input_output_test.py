#with open('weather.csv', 'r') as reader:
#    data = reader.read()
#print data

# print line by line

#with open('weather.csv', 'r') as reader:
#    data = reader.readline()
#    while data !='':
#        print data
#        data = reader.readline()
#print "It's over"

#for loop to grab only the rainfall values
'''
with open('weather.csv') as reader:
    data = reader.readline()
    rain = []
    for line in reader.readlines():
        r = line.strip().split(",")[-1]
	r = float(r)
	rain.append(r)

print rain

with open("myrain.txt", "w") as writer:
    for r in rain:
	writer.write(str(r) + "\n")
'''


#writting and reading binary data
'''
import struct

bin_data = struct.pack("bbbb", 123, 12, 45, 34)

with open("mybinary.dat", "wb") as writer:
    writer.write(bin_data)

with open("mybinary.dat", "rb") as reader:
    bin_data2 = reader.read()

data = struct.unpack("bbbb", bin_data2)

print data
'''



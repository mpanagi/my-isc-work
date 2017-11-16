#collect up counts using a dictionary
'''
band = ["mel", "geri", "victoria", "mel", "emma"]
counts = {}

for name in band:
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] += 1

for name in counts:
	print name, counts[name]
'''

# useful characteristics of dictionaries

if {}: print 'hi'
d = {"maggie": "uk", "ronnie": "usa"}

print d.items()
print d.keys()
print d.values()

#help(d.get)

print d.get("maggie", "nowhere")

print d.get("ringo", "nowhere")

res = d.setdefault("tom", "ussr")
print res, d["tom"]


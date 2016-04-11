def newfunc(fp):
	buff =""
	buff = buff + fp.read(20)
	print buff


fp = open("output.txt" , "r")

newfunc(fp)
newfunc(fp)
newfunc(fp)

a = "sdasdsadsad"+unichr(254)+"asdfasdf"
print a.find(unichr(254))
print a[0:11] + a[12:]
print unichr(254)
#print fp.read(20)
#print fp.read(20)
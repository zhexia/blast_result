import sys

fo = open(sys.argv[1]+".coverage", "w")

lengthDict = {}
with open(sys.argv[2]) as length:
	for line in length:
		info = line.split()
		lengthDict[info[0]] = int(info[1])
	
with open(sys.argv[1]) as blast:
	for line in blast:
		info = line.split()
		cov = (int(info[7])-int(info[6])+1)*100/lengthDict[info[0]]
		#print(int(info[7])-int(info[6])+1)
		fo.write("\t".join(info+[str('%.2f'%cov)+"%\n"]))

blast.close()
length.close()
fo.close()

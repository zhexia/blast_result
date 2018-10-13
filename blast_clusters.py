import sys
import os
from collections import defaultdict

gap = 4000
path = sys.argv[1].split('.')[0]
if not os.path.exists(path): os.mkdir(path) 
lncRNA = ""
lncDict = {}
with open(sys.argv[1]) as f:
	for line in f:
		lineinfo = line.split("\t")
		if lineinfo[0] != lncRNA:
			lncDict[lineinfo[0]] = defaultdict(list)			
			lncRNA = lineinfo[0]
		lineinfo[8] = int(lineinfo[8])
		lineinfo[9] = int(lineinfo[9])
		if lineinfo[8] < lineinfo[9]:
			lncDict[lineinfo[0]][lineinfo[1]].append((lineinfo[8],lineinfo[9],line))
		else:
			lncDict[lineinfo[0]][lineinfo[1]].append((lineinfo[9],lineinfo[8],line))

for (key,value) in lncDict.items():
	fo = open(path+"/"+key+".txt", "w")
	for chrom,loci in value.items():
		index = -gap
		for locusnum in sorted(loci):
			if locusnum[0] > index+gap:
				fo.write("\n")
			#fo.write("\t".join([key,chrom,str(locusnum[0]),str(locusnum[1])+"\n"]))
			fo.write(locusnum[2])
			index = locusnum[1]
		fo.write("-"*100+"\n")

f.close()
fo.close()

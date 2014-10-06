#!/usr/bin/env python
# coding=utf-8

def greedyHeurstic(n, M, W, C):
	ratio = []
	backpack = []
	weight = 0
	print W
	for index, element in W:
		ratioElement.weightIndex = index
		ratioElement.ratio = C[index]/W[index]
		ratio.append(ratioElement)
	ratio.sort()
	indexCounter = n - 1
	while (sum(backpack) + W[ratio[n].weightIndex]) <= M:
		backpack.append(W[ratio[n].weightIndex])
		n -= 1

	greedyWeight = sum(backpack)
	for element in backpack:
		greedyCost += C[element]

	print "greedyWeight = ", greedyWeight, "greedyCost = ", greedyCost



ans = []
myAns = []
for line in open('sol/knap_4.sol.dat', 'r'):
	lineArr = line.rstrip().split(' ')
	ans.append(''.join(lineArr[3:len(lineArr)]))

for line in open('inst/knap_4.inst.dat', 'r'):
	lineArr = line.rstrip().split(' ')
	n = int(lineArr[1])
	M = int(lineArr[2])
	W = []
	C = []
	i = 0
	while i < n:
		W.append(int(lineArr[2*i+3]))
		C.append(int(lineArr[2*i+3+1]))
		i += 1

	greedyHeurstic(n, M, W, C)
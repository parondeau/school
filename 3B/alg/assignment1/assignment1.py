#!/usr/bin/env python
# coding=utf-8

def binaryBruteForce(n, M, W, C):
	# integer n (# of items)
	# integer M (the capacity of the knapsack)
	# finite set W = {w1, w2, … ,wn } (weights of items)
	# finite set C = {c1, c2, … ,cn } (costs of items)
	count = 0
	maxCost = 0
	while count < 2**n:
		binCount = [int(l) for l in bin(count)[2:]]
		while len(binCount) < n:
			binCount.insert(0, 0)
		# print "count = ", count, "bincount = ", binCount
		curWeight = 0
		curCost = 0
		for index, val in enumerate(binCount):
			if val == 1:
				curWeight += W[index]
				curCost += C[index]
				# print "w, c", curWeight, curCost
		if curCost > maxCost and curWeight <= M:
			maxCost = curCost
			X = binCount
			# print "maxCost", maxCost
		count += 1

	# print 'maxCost=', maxCost
	# print 'X=', X
	myAns.append(''.join(map(str, X)))
	if len(myAns) == len(ans):
		# print "myAns=", myAns
		# print "ans=", ans
		for index, element in enumerate(ans):
			if ans[index] != myAns[index]:
				print "index", index, "does not work"
				print myAns[index]
		if myAns == ans:
			print "it's fuckin fine"

ans = []
myAns = []
for line in open('sol/knap_10.sol.dat', 'r'):
	lineArr = line.rstrip().split(' ')
	ans.append(''.join(lineArr[3:len(lineArr)]))

for line in open('inst/knap_10.inst.dat', 'r'):
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

	binaryBruteForce(n, M, W, C)
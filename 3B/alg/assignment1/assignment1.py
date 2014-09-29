#!/usr/bin/env python
# coding=utf-8

def binaryBruteForce(n, M, W, C):
	# integer n (# of items)
	# integer M (the capacity of the knapsack)
	# finite set W = {w1, w2, … ,wn } (weights of items)
	# finite set C = {c1, c2, … ,cn } (costs of items)
	count = 0
	maxCost = 0
	print "n=", 2**n
	print 'M=', M
	print 'W=',W
	print 'C=', C
	while count < 2**n:
		binCount = [int(l) for l in bin(count)[2:]]
		curWeight = 0
		curCost = 0
		for index, val in enumerate(binCount):
			if val == 1:
				curWeight += W[index]
				curCost += C[index]
		if curCost > maxCost and curWeight <= M:
			maxCost = curCost
			X = binCount
			while len(X) < n:
				X.append(0)
		count += 1

	print 'maxCost=', maxCost
	print 'X=', X
	return

# binaryBruteForce(5,10,[1,10,3,4,5],[5,4,3,2,1])
for line in open('sol/knap_4.sol.dat', 'r')


for line in open('inst/knap_4.inst.dat', 'r'):
	lineArr = line.rstrip().split(' ')
	n = int(lineArr[1])
	M = int(lineArr[2])
	W = []
	C = []
	i = 0
	while i < n:
		W.append(int(lineArr[i+3]))
		C.append(int(lineArr[n+i+3]))
		i += 1
	print n,M,W,C

	binaryBruteForce(n, M, W, C)




# M = 0
# totalWeight = 0
# totalCost = 0
# finalX = []
# maxCost = 0


# def brute(n, M, W, C):
# 	X = [0] * n
# 	recursiveCheck(n, W, C, X)
# 	print finalX
# 	return True

# def recursiveCheck(n, W, C, X):
# 	print X
# 	for index, item in enumerate(W):
# 		if X[index] == 0:

# 			print index

# 			if totalWeight + W[index] < M:
# 				totalWeight += W[index]
# 				totalCost += C[index]
# 				X[index] = 1
# 			recursiveCheck(n, W, C, X)
# 		elif index == n - 1:
# 			if totalCost > maxCost:
# 				maxCost = totalCost
# 				finalX = X
# 			X = [0] * n
# 			break

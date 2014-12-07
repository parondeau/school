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
		# prepend 0's to binary counter
		while len(binCount) < n:
			binCount.insert(0, 0)

		curWeight = 0
		curCost = 0
		# iterate through binary counter adding values assigned a 1 to the variables keeping track of weight and cost
		for index, val in enumerate(binCount):
			if val == 1:
				curWeight += W[index]
				curCost += C[index]

		# check if the new values are better than the previous max but still within constraints
		if curCost > maxCost and curWeight <= M:
			maxCost = curCost
			X = binCount
		count += 1
	# print maxCost
	# # used to check solution with answers
	# myAns.append(''.join(map(str, X)))
	# if len(myAns) == len(ans):
	# 	for index, element in enumerate(ans):
	# 		if ans[index] != myAns[index]:
	# 			# TODO
	# 			# compare two arrays and see if the item that doesn't work is a 0
	# 			print "line", index, "does not work"
	# 			print myAns[index]
	# 	if myAns == ans:
	# 		print "Everything works as expected"


# ans = []
# myAns = []

# for line in open('sol/knap_4.sol.dat', 'r'):
# 	lineArr2 = line.rstrip().split(' ')
# 	ans.append(''.join(lineArr2[3:len(lineArr2)]))

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

	binaryBruteForce(n, M, W, C)
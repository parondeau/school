#!/usr/bin/env python
# coding=utf-8
import sys
def bAndB(M, W, C):

	# M - knapsack size
	# W - weight of items undecided
	# C - cost of items undecided

	global totalW
	global totalC
	global bestC
	if len(W) > 0:
		# pruning time
		# cost function
		if totalC + sum(C) > bestC:
			# item in bag
			curItemW = W.pop(0)
			curItemC = C.pop(0)
			if totalW < M:
				totalW = totalW + curItemW
				totalC = totalC + curItemC

				bAndB(M, W, C)
				# item not in bag
				totalW = totalW - curItemW
				totalC = totalC - curItemC

			bAndB(M, W, C)
			W.insert(0, curItemW)
			C.insert(0, curItemC)
	else:
		if bestC < totalC and totalW <= M:
			bestC = totalC

totalW = 0
totalC = 0
bestC = 0

for line in open('inst/' + sys.argv[1], 'r'):
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

	bestC = 0
	bAndB(M, W, C)
	# print bestC

#!/usr/bin/env python
# coding=utf-8

def dynamic(M, W, C):

	# M - knapsack size
	# W - weight of items undecided
	# C - cost of items undecided

	global totalW
	global totalC
	global bestC
	# print M
	if len(W) > 0:
		# item in bag
		curItemW = W.pop(0)
		curItemC = C.pop(0)
		M = M - curItemW
		totalC = totalC + curItemC
		dynamic(M, W, C)
		# item not in bag

		M = M + curItemW
		totalC = totalC - curItemC
		dynamic(M, W, C)
		W.insert(0, curItemW)
		C.insert(0, curItemC)
	else:
		# print "totalC =", totalC
		# print "M =", M
		if M >= 0 and bestC < totalC:
			bestC = totalC



totalW = 0
totalC = 0
bestC = 0

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

# M = 100
# W = [18, 42, 88, 3]
# C = [114, 136, 192, 223]
	bestC = 0
	dynamic(M, W, C)
	print bestC

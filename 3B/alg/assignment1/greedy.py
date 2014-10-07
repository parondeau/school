#!/usr/bin/env python
# coding=utf-8
from array import array

class RatioElement(object):
	index = 0
	ratio = 0
	def __init__(self, index, ratio):
		self.index = index
		self.ratio = ratio

def greedyHeurstic(n, M, W, C):
	print W
	ratio = []
	backpack = []
	weight = 0
	for index, element in enumerate(W):
		ratioEle = RatioElement(index, C[index]/W[index])
		ratio.append(ratioEle)
	ratio.sort()
	indexCounter = n - 1
	print ratio
	# print ratio[indexCounter].index
	# print W[ratio[indexCounter].index]
	while (sum(backpack) + W[ratio[indexCounter].index]) <= M:
		backpack.append(W[ratio[indexCounter].index])
		n -= 1

	print backpack
	greedyWeight = sum(backpack)
	greedyCost = 0
	for index, element in enumerate(backpack):
		greedyCost += C[element]

	# print "greedyWeight = ", greedyWeight, "greedyCost = ", greedyCost


def greedyHeuristicRemove(n, M, W, C):
	# initialize variables
	# use floating point array to track ratio
	ratio = array('f')
	backpack = []
	greedyWeight = 0
	greedyCost = 0
	# calculate ratio of each element, store in array
	for index, element in enumerate(W):
		ratio.append(C[index]/W[index])

	# keep track of the location of the max ratio
	maxRatioIndex = ratio.index(max(ratio))
	# keep filling the backpack until an item does not fit (too heavy)
	while len(W) > 0 and greedyWeight + W[maxRatioIndex] < M:
		# increment the weight and cost of the items in the backpack
		greedyWeight += W[maxRatioIndex]
		greedyCost += C[maxRatioIndex]
		# remove elements added to backpack
		del W[maxRatioIndex]
		del C[maxRatioIndex]
		ratio.remove(max(ratio))
		# find new max ratio element
		if len(ratio) > 0:
		 	maxRatioIndex = ratio.index(max(ratio))

	myAns.append(int(greedyCost))
	if len(ans) == len(myAns):
		for index, element in enumerate(ans):
			if int(ans[index]) < myAns[index]:
				print "something is definitely wrong, the greedy algorithm did better than brute force"

ans = []
myAns = []
for line in open('sol/knap_40.sol.dat', 'r'):
	lineArr = line.rstrip().split(' ')
	ans.append(lineArr[2])

for line in open('inst/knap_40.inst.dat', 'r'):
	lineArr = line.rstrip().split(' ')
	n = int(lineArr[1])
	M = int(lineArr[2])
	W = []
	C = []
	i = 0
	while i < n:
		W.append(float(lineArr[2*i+3]))
		C.append(float(lineArr[2*i+3+1]))
		i += 1

	greedyHeuristicRemove(n, M, W, C)
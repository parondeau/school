#!/usr/bin/env python
# coding=utf-8
import sys
from random import getrandbits, uniform, randint
from math import exp
from decimal import *

def simAnn(n, M, W, C):
	# params
	INITIAL_TEMP = 100 * int(sys.argv[2])
	FINAL_TEMP = 100
	ALPHA = float(sys.argv[3])/100
	INNER_LOOP_STEPS = int(sys.argv[4])
	INITIAL_STATE = constructInitialState(n)

	highestCost = 0

	t = INITIAL_TEMP
	state = INITIAL_STATE
	while ( t > FINAL_TEMP ):
		for i in xrange( INNER_LOOP_STEPS ):
			new = random_neighbour(state, n)
			new = repair(new, M)

			newCost = cost(new)
			if newCost > highestCost: highestCost = newCost

			delta_C = newCost - cost(state)
			if ( delta_C > 0 ):
				state = new
			elif (accept(delta_C, t)):
				state = new

		t = cool(t, ALPHA)

	# error checking stuff
	myAns.append(highestCost)
	if len(ans) == len(myAns):
		for index, element in enumerate(ans):
			print Decimal(1) - ((Decimal(ans[index]) - Decimal(myAns[index]) ) / Decimal(ans[index]))
			if int(ans[index]) < myAns[index]:
				print "something is definitely wrong, the greedy algorithm did better than brute force"

def accept(delta_C, t):
	if (t == 0): return 0
	return uniform(0,1) < exp(-abs(delta_C) / t)

def repair(state, M):
	while not (feasible(state, M)):
		itemIndex = randint(0, n-1)
		state[itemIndex] = 0
	return state

def feasible(state, M):
	weight = getWeight(state)
	return weight <= M

def cool(t, alpha):
	return t*alpha

def random_neighbour(state, n):
	new = list(state)
	# generate random index for state array
	itemIndex = randint(0, n-1)
	# flip the bit to generate new state
	new[itemIndex] = (new[itemIndex] + 1) % 2
	return new

def cost(state):
	cost = 0
	for index, value in enumerate(state):
		cost += value * C[index]
	return cost

def getWeight(state):
	weight = 0
	for index, value in enumerate(state):
		weight += value * W[index]
	return weight

def constructInitialState(n):
	state = []
	# convert random number into binary string
	stateStr = "{0:b}".format(getrandbits(n))
	for index, value in enumerate(stateStr):
		state.append(int(value))
	while len(state) < n:
		state.insert(0, 0)
	return state


ans = []
myAns = []
getcontext().prec = 2
for line in open('sol/knap_' + sys.argv[1] + '.sol.dat', 'r'):
	lineArr = line.rstrip().split(' ')
	ans.append(lineArr[2])

for line in open('inst/knap_' + sys.argv[1] + '.inst.dat', 'r'):
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

	simAnn(n, M, W, C)


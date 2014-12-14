#!/usr/bin/env python
# coding=utf-8
import sys
from random import getrandbits, uniform, randint
from math import exp
from decimal import *

# n = the number of variables
# C = cost(weights) of each variable


def simAnn(n, C):
	# params
	INITIAL_TEMP = 100 * int(sys.argv[2])
	INITIAL_TEMP = 200
	FINAL_TEMP = 100
	ALPHA = float(sys.argv[3])/100
	INNER_LOOP_STEPS = int(sys.argv[4])
	INITIAL_STATE = constructInitialState(n)

	highestCost = 0

	t = INITIAL_TEMP
	state = INITIAL_STATE
	while ( t > FINAL_TEMP ):
		for i in xrange( INNER_LOOP_STEPS ):
			new = random_neighbour(state)
			new = repair(new)

			newCost = cost(new)
			if newCost > highestCost: highestCost = newCost

			delta_C = newCost - cost(state)
			if ( delta_C > 0 ):
				state = new
			elif (accept(delta_C, t)):
				state = new

		t = cool(t, ALPHA)
	print highestCost

def random_neighbour(state):
	new = list(state)
	# generate random index for state array
	itemIndex = randint(0, n-1)
	# flip the bit to generate new state
	new[itemIndex] = new[itemIndex] ^ 1
	return new

def repair(state):
	while not (feasible(state)):
		itemIndex = randint(0, n-1)
		state[itemIndex] = state[itemIndex] ^ 1
	return state

def feasible(state):
	for index, clause in enumerate(maxSAT):
		tmpArr = [0 for x in xrange(n)]
		for index, value in enumerate(clause):
			tmpArr[abs(value) - 1] = 1 if value > 0 else 0

		if not ((state[0] == tmpArr[0] ) or (state[1] == tmpArr[1] ) or (state[2] == tmpArr[2] )):
			return False
	return True

def cost(state):
	cost = 0
	for index, value in enumerate(state):
		cost += value * C[index]
	return cost

def accept(delta_C, t):
	if (t == 0): return 0
	return uniform(0,1) < exp(-abs(delta_C) / t)

def cool(t, alpha):
	return t*alpha

def constructInitialState(n):
	state = []
	# convert random number into binary string
	stateStr = "{0:b}".format(getrandbits(n))
	for index, value in enumerate(stateStr):
		state.append(int(value))
	while len(state) < n:
		state.insert(0, 0)
	return state

maxSAT = []
for line in open('inst/maxSAT_3_' + sys.argv[1] + '.dimacs', 'r'):
	lineArr = line.rstrip().split(' ')
	# trim the zero
	lineArr.pop()
	lineIntArr = [ int(x) for x in lineArr ]
	maxSAT.append(lineIntArr)
	del lineArr
	del lineIntArr

for line in open('inst/maxSAT_weights.txt', 'r'):
	lineArr = line.rstrip().split(' ')
	n = len(maxSAT[0])
	C = [int(x) for x in lineArr]

	simAnn(n, C)

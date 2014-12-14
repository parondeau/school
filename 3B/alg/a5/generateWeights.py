#!/usr/bin/env python
# coding=utf-8

from random import randint

with open('maxSAT_weights.txt', 'w') as myfile:
    for x in range(50):
    	line = str(randint(0, 10)) + ' ' + str(randint(0, 10)) + ' ' + str(randint(0, 10)) + '\n'
    	myfile.write(line)

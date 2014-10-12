#!/bin/bash
for Y in {1..15}
do
	START=$(gdate +%s%3N)
	python assignment1.py
	FINISH=$(gdate +%s%3N)
	echo $((FINISH - START))
done
echo
for Y in {1..15}
do
	START=$(gdate +%s%3N)
	python greedy.py
	FINISH=$(gdate +%s%3N)
	echo $((FINISH - START))
done

#!/bin/bash
for Y in {1..15}
do
	START=$(gdate +%s%3N)
	python bandb.py > bandb.txt
	FINISH=$(gdate +%s%3N)
	echo Time in ms to complete 15 instances:  $((FINISH - START))
done
echo
for Y in {1..15}
do
	START=$(gdate +%s%3N)
	python ../assignment1/assignment1.py > brute.txt
	FINISH=$(gdate +%s%3N)
	echo Time in ms to complete 15 instances: $((FINISH - START))
done

diff bandb.txt brute.txt
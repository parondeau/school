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
	python dynamic.py > dynamic.txt
	FINISH=$(gdate +%s%3N)
	echo Time in ms to complete 15 instances: $((FINISH - START))
done

diff bandb.txt dynamic.txt
rm bandb.txt
rm dynamic.txt

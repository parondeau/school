#!/bin/bash
for Y in {1..15}
do
	START=$(gdate +%s%3N)
	# for X in {1..25}
	# do
		python assignment1.py
	# done
	# echo "Total time (ms) for 50 trials =" $((FINISH - START))
	FINISH=$(gdate +%s%3N)
	echo $((FINISH - START))
done
echo
for Y in {1..15}
do
	START=$(gdate +%s%3N)
	# for X in {1..25}
	# do
		python greedy.py
	# done
	# echo "Total time (ms) for 50 trials =" $((FINISH - START))
	FINISH=$(gdate +%s%3N)
	echo $((FINISH - START))
done
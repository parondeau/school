#!/bin/bash
# for Y in {1..15}
# do
# 	START=$(gdate +%s%3N)
# 	python bandb.py > bandb.txt
# 	FINISH=$(gdate +%s%3N)
# 	echo Time in ms to complete 50 instances:  $((FINISH - START))
# 	# echo $((FINISH - START))
# done
# echo
# for Y in {1..15}
# do
# 	START=$(gdate +%s%3N)
# 	python dynamic.py > dynamic.txt
# 	FINISH=$(gdate +%s%3N)
# 	echo Time in ms to complete 50 instances: $((FINISH - START))
# 	# echo $((FINISH - START))
# done
# echo
for Y in {1..15}
do
	START=$(gdate +%s%3N)
	python fptas.py > fptas.txt
	FINISH=$(gdate +%s%3N)
	# echo Time in ms to complete 50 instances: $((FINISH - START))
	echo $((FINISH - START))
done

# echo diff bandb with dynamic
# diff bandb.txt dynamic.txt
# echo
# echo diff dynamic with fptas
# diff dynamic.txt fptas.txt
# rm bandb.txt
# rm dynamic.txt
# rm fptas.txt

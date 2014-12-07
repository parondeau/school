#!/bin/bash
sizeArr=(4 8 10 15 20 40)
maxWeightAndCostArr=(20 40 100 200 1000)
granArr=(10 25 50 75 99 200)
knapArr=(10 20 50 75 99 200)

mv greedy_results.txt greedy_results_old.txt
touch greedy_results.txt
(tail -f greedy_results.txt & echo $! >&3) 3>pid
echo GREEDY >> greedy_results.txt
echo Varying Size >> greedy_results.txt
for i in "${sizeArr[@]}"
do
	fileName=size$i.txt
	START=$(gdate +%s%3N)
	python algs/greedy.py $fileName
	FINISH=$(gdate +%s%3N)
	echo n=$i N=50 m=0.5 W=100 C=100 k=0.5 d=0 '|' $((FINISH - START)) >> greedy_results.txt
done
echo Varying Weight >> greedy_results.txt
for i in "${maxWeightAndCostArr[@]}"
do
	fileName=maxWeight$i.txt
	START=$(gdate +%s%3N)
	python algs/greedy.py $fileName
	FINISH=$(gdate +%s%3N)
	echo n=10 N=50 m=0.5 W=$i C=100 k=0.5 d=0 '|' $((FINISH - START)) >> greedy_results.txt
done
echo Varying Cost >> greedy_results.txt
for i in "${maxWeightAndCostArr[@]}"
do
	fileName=maxCost$i.txt
	START=$(gdate +%s%3N)
	python algs/greedy.py $fileName
	FINISH=$(gdate +%s%3N)
	echo n=10 N=50 m=0.5 W=100 C=$i k=0.5 d=0 '|' $((FINISH - START)) >> greedy_results.txt
done
echo Varying CapToW >> greedy_results.txt
for i in "${knapArr[@]}"
do
	fileName=knapCapToW$i.txt
	START=$(gdate +%s%3N)
	python algs/greedy.py $fileName
	FINISH=$(gdate +%s%3N)
	if [ "$i" = "200" ]; then
		echo n=10 N=50 m=2 W=100 C=100 k=0.5 d=0 '|' $((FINISH - START)) >> greedy_results.txt
	else
		echo n=10 N=50 m=0.$i W=100 C=100 k=0.5 d=0 '|' $((FINISH - START)) >> greedy_results.txt
	fi
done
echo Varying Gran >> greedy_results.txt
for i in "${granArr[@]}"
do
	fileName=gran$i.txt
	START=$(gdate +%s%3N)
	python algs/greedy.py $fileName
	FINISH=$(gdate +%s%3N)
	if [ "$i" = "200" ]; then
		echo n=10 N=50 m=0.5 W=100 C=100 k=2 d=0 '|' $((FINISH - START)) >> greedy_results.txt
	else
		echo n=10 N=50 m=0.5 W=100 C=100 k=0.$i d=0 '|' $((FINISH - START)) >> greedy_results.txt
	fi
done
kill $(<pid)
rm pid

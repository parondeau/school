#!/bin/bash
sizeArr=(4 8 10 15 20 40)
maxWeightAndCostArr=(20 40 100 200 1000)
granArr=(10 25 50 75 99 200)
knapArr=(10 20 50 75 99 200)

mv dynamic_results.txt dynamic_results_old.txt
touch dynamic_results.txt
(tail -f dynamic_results.txt & echo $! >&3) 3>pid
echo DYNAMIC >> dynamic_results.txt
echo Varying Size >> dynamic_results.txt
for i in "${sizeArr[@]}"
do
	fileName=size$i.txt
	START=$(gdate +%s%3N)
	python algs/dynamic.py $fileName
	FINISH=$(gdate +%s%3N)
	echo n=$i N=50 m=0.5 W=100 C=100 k=0.5 d=0 '|' $((FINISH - START)) >> dynamic_results.txt
done
echo Varying Weight >> dynamic_results.txt
for i in "${maxWeightAndCostArr[@]}"
do
	fileName=maxWeight$i.txt
	START=$(gdate +%s%3N)
	python algs/dynamic.py $fileName
	FINISH=$(gdate +%s%3N)
	echo n=10 N=50 m=0.5 W=$i C=100 k=0.5 d=0 '|' $((FINISH - START)) >> dynamic_results.txt
done
echo Varying Cost >> dynamic_results.txt
for i in "${maxWeightAndCostArr[@]}"
do
	fileName=maxCost$i.txt
	START=$(gdate +%s%3N)
	python algs/dynamic.py $fileName
	FINISH=$(gdate +%s%3N)
	echo n=10 N=50 m=0.5 W=100 C=$i k=0.5 d=0 '|' $((FINISH - START)) >> dynamic_results.txt
done
echo Varying CapToW >> dynamic_results.txt
for i in "${knapArr[@]}"
do
	fileName=knapCapToW$i.txt
	START=$(gdate +%s%3N)
	python algs/dynamic.py $fileName
	FINISH=$(gdate +%s%3N)
	if [ "$i" = "200" ]; then
		echo n=10 N=50 m=2 W=100 C=100 k=0.5 d=0 '|' $((FINISH - START)) >> dynamic_results.txt
	else
		echo n=10 N=50 m=0.$i W=100 C=100 k=0.5 d=0 '|' $((FINISH - START)) >> dynamic_results.txt
	fi
done
echo Varying Gran >> dynamic_results.txt
for i in "${granArr[@]}"
do
	fileName=gran$i.txt
	START=$(gdate +%s%3N)
	python algs/dynamic.py $fileName
	FINISH=$(gdate +%s%3N)
	if [ "$i" = "200" ]; then
		echo n=10 N=50 m=0.5 W=100 C=100 k=2 d=0 '|' $((FINISH - START)) >> dynamic_results.txt
	else
		echo n=10 N=50 m=0.5 W=100 C=100 k=0.$i d=0 '|' $((FINISH - START)) >> dynamic_results.txt
	fi
done
kill $(<pid)
rm pid

#!/bin/bash
sizeArr=(4 8 10 15 20 40)
maxWeightAndCostArr=(20 40 100 200 1000)
granArr=(10 25 50 75 99 200)
knapArr=(10 20 50 75 99 200)

touch dynamic_error_results.txt
echo DYNAMIC >> dynamic_error_results.txt
echo Varying Size >> dynamic_error_results.txt
for i in "${sizeArr[@]}"
do
	fileName=size$i.txt
	python algs/dynamic.py $fileName >> dynamic_error_results.txt
done
echo Varying Weight >> dynamic_error_results.txt
for i in "${maxWeightAndCostArr[@]}"
do
	fileName=maxWeight$i.txt
	python algs/dynamic.py $fileName >> dynamic_error_results.txt
done
echo Varying Cost >> dynamic_error_results.txt
for i in "${maxWeightAndCostArr[@]}"
do
	fileName=maxCost$i.txt
	python algs/dynamic.py $fileName >> dynamic_error_results.txt
done
echo Varying CapToW >> dynamic_error_results.txt
for i in "${knapArr[@]}"
do
	fileName=knapCapToW$i.txt
	python algs/dynamic.py $fileName >> dynamic_error_results.txt
done
echo Varying Gran >> dynamic_error_results.txt
for i in "${granArr[@]}"
do
	fileName=gran$i.txt
	python algs/dynamic.py $fileName >> dynamic_error_results.txt
done

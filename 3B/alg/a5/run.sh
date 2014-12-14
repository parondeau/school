#!/bin/bash
sizeArr=(1 2 4)
tempRatio=(2 4 5 7 10)
alpha=(80 85 90 95 99)
innerLoop=(1 5 10 50 100)

defaultSize=4
defaultTempRatio=5
defaultAlpha=80
defaultInnerLoop=1

for i in "${sizeArr[@]}"
do
	echo Running $i Knapsack

	START=$(gdate +%s%3N)
	python maxSAT.py $i $defaultTempRatio $defaultAlpha $defaultInnerLoop > results/simAnnResults_$i.txt
	FINISH=$(gdate +%s%3N)
	echo $i $defaultTempRatio $defaultAlpha $defaultInnerLoop '|' $((FINISH - START)) > results/simAnnResults_timing.txt

done
for i in "${tempRatio[@]}"
do
	echo Running Temp Ratio $i Knapsack

	START=$(gdate +%s%3N)
	python maxSAT.py $defaultSize $i $defaultAlpha $defaultInnerLoop > results/simAnnResults_temp_$i.txt
	FINISH=$(gdate +%s%3N)
	echo $defaultSize $i $defaultAlpha $defaultInnerLoop '|' $((FINISH - START)) >> results/simAnnResults_timing.txt

done
for i in "${alpha[@]}"
do
	echo Running Alpha $i Knapsack

	START=$(gdate +%s%3N)
	python maxSAT.py $defaultSize $defaultTempRatio $i $defaultInnerLoop > results/simAnnResults_alpha_$i.txt
	FINISH=$(gdate +%s%3N)
	echo $defaultSize $defaultTempRatio $i $defaultInnerLoop '|' $((FINISH - START)) >> results/simAnnResults_timing.txt
done
for i in "${innerLoop[@]}"
do
	echo Running Inner Loop $i Knapsack

	START=$(gdate +%s%3N)
	python maxSAT.py $defaultSize $defaultTempRatio $defaultAlpha $i > results/simAnnResults_innerLoop_$i.txt
	FINISH=$(gdate +%s%3N)
	echo $defaultSize $defaultTempRatio $defaultAlpha $i '|' $((FINISH - START)) >> results/simAnnResults_timing.txt
done

#!/bin/bash
CORES=40
START=4
for ((i=0;i<CORES;i++)); do
	PORT=$(( 8601 + $i ))
	cmd="nohup taskset -c $(( $START + $i )) npx hardhat node --port $PORT &> logs/hardhat.$PORT &"
	echo $cmd
	eval $cmd
	pid=$!
done
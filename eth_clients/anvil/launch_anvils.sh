#!/bin/bash
CORES=24
for ((i=0;i<CORES;i++)); do
	PORT=$(( 8544 - $i ))
	cmd="nohup anvil --fork-url http://localhost:8545 --fork-block-number 14000007 --port $PORT --order fifo &> logs/anvil.$PORT &"
	echo $cmd
	eval $cmd
done

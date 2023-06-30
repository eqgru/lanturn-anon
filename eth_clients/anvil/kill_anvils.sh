#!/bin/bash
CORES=24
for ((i=0;i<CORES;i++)); do
	PORT=$(( 8544 - $i ))
	pid=`ps -ef | grep anvil | grep fork | grep $PORT | awk {'print $2'}`
	echo $PORT $pid
	kill -s SIGTERM $pid
done
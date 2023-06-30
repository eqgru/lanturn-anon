#!/bin/bash
PORT=$1
pid=`ps -ef | grep anvil | grep fork | grep $PORT | awk {'print $2'}`
echo $pid
kill -s SIGTERM $pid
nohup anvil --fork-url http://localhost:8545 --fork-block-number 14000007 --port $PORT --order fifo &> logs/anvil.$PORT &

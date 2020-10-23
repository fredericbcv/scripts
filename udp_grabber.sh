#!/bin/bash

# Exit function
trap ctrl_c INT

function ctrl_c() {
	echo "#Trapped: CTRL-C"
	rm $udp_path"/"tmp_file
	exit 0
}

# Check if parameter exist
if [ -z $1 ] || [ -z $2 ]
then
	echo "#ERROR: Missing parameters"
	echo "Usage: ./udp_grabber.sh [PORT] [PATH]"
	exit 1
fi

# Check parameter value
if [ "$1" -lt 1 ] || [ "$1" -gt 65535 ]
then
	echo "#ERROR: Port must be equal from 1 to 65535"
	exit 1
fi

udp_port=$1

# Check if path exist
if [ ! -d $2 ]
then
	echo "#ERROR: Path does not exists"
	exit 1
fi

udp_path=$2

while :
do
	nc -l -W1 -u $udp_port > $udp_path"/"tmp_file
	packet_name=$(date +"%Y-%m-%d_%k:%M:%S_%N_udp_payload")
	mv $udp_path"/"tmp_file $udp_path"/"$packet_name
done

exit 0

#!/bin/bash

# Check if enough arguments are passed
if [ "$#" -lt 3 ]; then
    echo "Usage: $0 <binary_path> <binary_args> <runs>"
    exit 1
fi

# Parameters
BINARY="$1"         # First argument is the binary path
ARGS="${@:2:$#-2}"  # All arguments except the first and the last
RUNS="${@: -1}"     # Last argument is the number of runs
TOTAL_TIME=0

for ((i=1; i<=RUNS; i++))
do
    OUTPUT=$($BINARY $ARGS)

    TIME=$(echo "$OUTPUT" | grep "Time" | awk '{print $2}')

    TOTAL_TIME=$(echo "$TOTAL_TIME + $TIME" | bc)

done

# Calculate the average
AVERAGE_TIME=$(echo "scale=7; $TOTAL_TIME / $RUNS" | bc)

echo "Average Time: $AVERAGE_TIME ms"

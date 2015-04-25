#!/bin/bash

# running command: $./removeDup /path to FB statuses/
mkdir -p ./Depression_nondupe

for k in $(find $1 -type f -name "*.txt")
do
filename=$(basename "$k")
extension="${filename##*.}"
filename="${filename%.*}"
cat $k | awk '!x[$0]++' | sed '/LikeUnlike/d' > ./Depression_nondupe/$filename"_d.txt"
done


#!/bin/bash

mkdir -p ./Depression_nondupe

for k in $(find $1 -maxdepth 1 -type f)
do
filename=$(basename "$k")
extension="${filename##*.}"
filename="${filename%.*}"
cat $k | awk '!x[$0]++' | sed '/LikeUnlike/d' > ./Depression_nondupe/$filename"_d.txt"
done


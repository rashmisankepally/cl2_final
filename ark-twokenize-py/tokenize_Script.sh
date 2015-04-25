#!/bin/bash

mkdir -p ./Depression_tokenized
for file in $(find $1 -type f -name "*.txt")
do
filename=$(basename "$file")
echo $filename
extension="${filename##*.}"
echo $extension
filename="${filename%.*}"
echo $filename
python twokenize.py $file > ./Depression_tokenized/$filename"_tokens.txt"
done


#!/bin/bash
echo "$(cut -c3 /dev/stdin)"

#i=1
#while read line || [ -n "$line" ];
#do
    #echo "$i - $line"
    #i=$(($i+1))
    #echo $line | iconv -f "UTF-8" -t "CP1252" | awk '{ split($0, chars, ""); print chars[3] }'
    #echo $line | awk '{ split($0, chars, ""); print chars[3] }'
#done

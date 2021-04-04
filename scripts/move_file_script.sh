#!/bin/bash
#filename='company.txt'
#n=1
#while read line; do
## reading each line
##echo "Line No. $n : $line"
##echo "Line No. $n"
#echo $line
#n=$((n+1))
#done < $filename

while read line; do
    echo "testing line $line"
#    find . -name "*$line*" -exec cp {} /Users/pruthvikumar/Documents/workspace/a1m/parkingspot-service/images_backup \;
done < ~/Desktop/attachement_ids.txt
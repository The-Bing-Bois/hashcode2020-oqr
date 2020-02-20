#!bin/sh
ls in > fileList.txt
while IFS= read -r document || [ -n "$document" ]
do
    python -m solver in/$document out/$document  
done < fileList.txt
#!
FILENAME=dob_`date +%Y-%m-%d`.csv
HEADERFILENAME=header_dob_`date +%Y-%m-%d`.csv
tmpRESULTFILENAME=tmp_result_dob_`date +%Y-%m-%d`.csv
RESULTFILENAME=result_dob_`date +%Y-%m-%d`.csv

curl "https://data.cityofnewyork.us/api/views/ipu4-2q9a/rows.csv?accessType=DOWNLOAD" > $FILENAME
head -1 $FILENAME  |sed "s/&/n/" | sed "s/Owner.s/Owners/" | sed "s/ /_/g" | sed "s/'//g" | sed "s/#/number/g" | sed "s/-/_/g" | sed "s/\.//g"  > $HEADERFILENAME
cp $HEADERFILENAME $tmpRESULTFILENAME
tail +2 $FILENAME >> $tmpRESULTFILENAME
cat $tmpRESULTFILENAME | ./process.dob.to.BIGQUERY.py > $RESULTFILENAME


# cat rows.csv | sed "s/ /_/g" | sed "s/'//g" | sed "s/#/number/g" | sed "s/-/_/g" | sed "s/\.//g" 

#  '<,'>s/ /_/g
# 10  '<,'>s/'//g
# 11  '<,'>s/#/number/g
# 13  '<,'>s/-/_/g
# 18  '<,'>s/\.//g

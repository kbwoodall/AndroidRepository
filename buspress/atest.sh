#!/bin/bash

echo running business press extracts
  
rm temp.csv buspress.csv

node getfiles.js accountingfirm
cat temp.csv  >> buspress.csv
cat null.csv  >> buspress.csv

rm temp.csv
node getfiles.js advertisingagency
cat temp.csv  >> buspress.csv
cat null.csv  >> buspress.csv

rm temp.csv
node getfiles.js angelfundinvestor
cat temp.csv  >> buspress.csv
cat null.csv  >> buspress.csv

echo end of business press extracts


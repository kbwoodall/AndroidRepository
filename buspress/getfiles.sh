#!/bin/bash

echo running business press extracts
rm temp.csv buspress.csv

firmname=(
 bankruptcyattorney 
 buscommlitigationattorney 
 criminalattorney
 gamingattorney
 generalpracticeattorney
 governmentaffairsattorney
 immigrationattorney
 intellectualpropertyattorney
 lawfirm
 litigationattorney
 locallawfirm 
 medicalmalpracticeattorney 
 nationallawfirm 
 personalinjuryattorney
)

arr=(accountingfirm
 advertisingagency 
 angelfundinvestor
 architecturefirm  
 automotivedealer
 businessbank
 casino
 casinovendor
 commercialdeveloper  
 commercialinsurance  
 commercialmortgage  
 commercialmovingcompany
 commercialprinting
 commercialpropertymanager
 commercialrealestate
 commercialresidentiallandscaper
 communitybank
 computerservice
 concierge
 constructioncompanycontractor
 conventionspace 
 cosmeticplasticsurgerypractice
 creditunion
 dayspa
 dentalcareprovider
 energycompany
 engineeringfirm 
 environmentalservices
 eventplanner
 execrecruiter
 familyownedbusiness
 filmvideoproductioncompany  
 financialadviser
 financialinstitution 
 fitnessrecreationcenter
 franchiser
 gamingsupplierscasinooperator
 graphicdesigncompany 
 greenbuilder
 greenserviceprovider 
 hispanicmedia
 hospital
 insurancebroker
 itserviceprovider
 largestemployer
 largestmanufacturer
 legalsupportservice 
 mediacompany 
 medicalgroup 
 minoritymediacompany
 minorityownedbusiness
 mortgagelender
 nationalbank
 officefurniture 
 officemachine 
 optometrist
 payrollcompany
 physicaltherapy
 professionalorg
 publicrelations
 residentialhomebuilder
 residentialrebroker
 residentialtopsalesagent 
 sbalender
 specialtyclinic 
 staffingfirm
 stockbroker
 technology
 telecommunications
 transportationservice
 treatmentcenter
 urgentcarecenter
 venturecapitalfirm
 wastemanagementservice
 wirelesscableprovider)  

m1=(
 assistedlivingfacility 
)
m2=(
 chamberofcommerce
)
m3=(
 charitableorganization
)
m4=(
 citycountybusinessservice
 municipalbusinessservice 
)
m5=(
 industrialpark
 officepark
)
m6=(
 laborunion
)
m7=(
 college
 professionalcertification
 privateschool
 graduateprogram
)
m8=(
 femalebusinessleader
 industryleader 
)
m9=(
 largestofficeindustrial
)
m10=(
 largestretail
)

m11=(
 minoritybusinessleader
)

m12=(
 networkinggroup
 pediatricgrouppractice
)

m13=(
 restaurant
)

m14=(
 shoppingcenter
)

m15=(
 topbankpresident
)

m16=(
 tradeassociation
)

m17=(
 tvanchor 
)

m18=(
 titlecompany
 pharmacy
 meetingfacility
)


for i in "${arr[@]}"
do
        node getfiles.js $i
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${firmname[@]}"
do
        node getfirms.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m1[@]}"
do
        node getm1.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m2[@]}"
do
        node getm2.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m3[@]}"
do
        node getm3.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m4[@]}"
do
        node getm4.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m5[@]}"
do
        node getm5.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m6[@]}"
do
        node getm6.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m7[@]}"
do
        node getm7.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m8[@]}"
do
        node getm8.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m9[@]}"
do
        node getm9.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m10[@]}"
do
        node getm10.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m11[@]}"
do
        node getm11.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m12[@]}"
do
        node getm12.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m13[@]}"
do
        node getm13.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m14[@]}"
do
        node getm14.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m15[@]}"
do
        node getm15.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m16[@]}"
do
        node getm16.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m17[@]}"
do
        node getm17.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done

for j in "${m18[@]}"
do
        node getm18.js $j
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done


echo end of business press extracts





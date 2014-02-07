#!/bin/bash

echo running business press extracts
rm temp.csv buspress.csv

other1=(
 minoritybusinessleader, full_name
 municipalbusinessservice department_name,
 networkinggroup, group_name
 officepark, property_name
 pediatricgrouppractice,group_name
 privateschool,school_name
 professionalcertification,school_name
 restaurant,restaurant_name
 shoppingcenter,mall_name
 topbankpresident,bank
 tradeassociation,association_name
 tvanchor, station 
 titlecompany, exec_first_name
 pharmacy, exec_first_name
 meetingfacility, exec_first_name

)
other=(
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
 wirelesscableprovider  
)

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
)
m5=(
 industrialpark
)
m6=(
 laborunion
)
m7=(
 college
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

arrname=(
 assistedlivingfacility 
 bankruptcyattorney 
 buscommlitigationattorney 
 chamberofcommerce
 charitableorganization
 citycountybusinessservice
 college
 criminalattorney
 femalebusinessleader
 gamingattorney
 generalpracticeattorney
 governmentaffairsattorney
 graduateprogram
 immigrationattorney
 industrialpark
 industryleader
 intellectualpropertyattorney
 laborunion
 largestofficeindustrial
 largestretail
 lawfirm
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
 meetingfacility
 minoritymediacompany
 minorityownedbusiness
 mortgagelender
 nationalbank
 officefurniture 
 officemachine 
 optometrist
 payrollcompany
 pharmacy
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
 titlecompany
 transportationservice
 treatmentcenter
 tvanchor,station 
 urgentcarecenter
 venturecapitalfirm
 wastemanagementservice
 wirelesscableprovider)  

for i in "${other[@]}"
do
        node getfiles.js $i
        cat temp.csv  >> buspress.csv
        cat null.csv  >> buspress.csv
done


echo end of business press extracts




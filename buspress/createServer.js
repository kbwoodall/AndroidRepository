
var Router = require('node-simple-router')
//172,17,5.110
//-----------------------------------------------------------------------------------------
var http   = require('http')
var router = Router();

var jsoncsv, data, fs, arrayOfJSON;
var mysql    = require('mysql');
var json2csv    = require('json2csv');

var pconnection = mysql.createConnection({
    host     : 'writer.mysql.stephensmedia.com',
    user     : 'django_project',
    password : 'lD*3.$~F2PM[', 
    database : 'django_bizproject',
    insecureAuth: true
});

    pconnection.connect();
//-----------------------------------------------------------------------------------------
var tm = function() {
    var date = new Date();
    var hour = date.getHours();
    hour = (hour < 10 ? "0" : "") + hour;
    var min  = date.getMinutes();
    min = (min < 10 ? "0" : "") + min;
    var sec  = date.getSeconds();
    sec = (sec < 10 ? "0" : "") + sec;
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    month = (month < 10 ? "0" : "") + month;
    var day  = date.getDate();
    day = (day < 10 ? "0" : "") + day;
    var ts = year + "-" + month + "-" + day + "-" + hour + "-" + min + "-" + sec;
    console.log("TIMESTAMP IS " + ts);
    return ts;
};
//-------------------------------------------------------------------------------------------
router.get('/', function (request, response) {
    var lst = 'accountingfirm' + '\n'   
        + 'accountingfirm' + '\n'   
        + 'accountingfirm' + '\n' ;
    response.end('List of tables\n' + slist);
})
//-------------------------------------------------------------------------------------------
router.get('/getcompanies', function (request, response) {
    response.end('Table not entered\n');
})
//-------------------------------------------------------------------------------------------
router.get('/getcompanies/:who', function(request, response) {

    //pconnection.connect();
    var sql = " ";
    var lst = "";
    var cat = request.params.who;
    var t1  = "bizforms_";
    var tbl = "bizforms_" + cat;

    var sql = 'select distinct ' + "\"" + cat + "\"" + ',company_name,address,zip,phone,exec_first_name,exec_last_name, exec_title, author_first_name, author_last_name,author_phone,author_email from ' + tbl + ' order by company_name, id desc';

    pconnection.query(sql, function(err, rows, fields) {
        if(err) { 
            response.end("Table not found");
        }
        else {
            var rtn = JSON.stringify(rows);
            var js = JSON.parse(rtn);
            js.forEach(function(item) {
               lst = lst + item.company_name + '\n' + '               ' +  item.address + ' ' + item.zip + '\n' + '               ' + item.phone + '\n' 
               + '               ' + item.exec_first_name + " " + item.exec_last_name + '\n'
               + '               ' + item.exec_title + '\n';
            });     
            response.end(lst);
       } 
    });
})

server = http.createServer(router)
server.listen(3000)
//-------------------------------------------------------------------------------------------

var slist='accountingfirm' + '\n' +
 'advertisingagency' + '\n' + 
 'angelfundinvestor' + '\n' +
 'architecturefirm' + '\n' +  
 'automotivedealer' + '\n' + 
 'businessbank' + '\n' + 
 'casino' + '\n' + 
 'casinovendor' + '\n' +
 'commercialdeveloper' + '\n' +   
 'commercialinsurance' + '\n' +   
 'commercialmortgage' + '\n' +   
 'commercialmovingcompany' + '\n' + 
 'commercialprinting' + '\n' + 
 'commercialpropertymanager' + '\n' + 
 'commercialrealestate' + '\n' + 
 'commercialresidentiallandscaper' + '\n' + 
 'communitybank' + '\n' + 
 'computerservice' + '\n' + 
 'concierge' + '\n' + 
 'constructioncompanycontractor' + '\n' + 
 'conventionspace' + '\n' + 
 'cosmeticplasticsurgerypractice' + '\n' + 
 'creditunion' + '\n' + 
 'dayspa' + '\n' + 
 'dentalcareprovider' + '\n' +
 'energycompany' + '\n' +
 'engineeringfirm' + '\n' + 
 'environmentalservices' + '\n' + 
 'eventplanner' + '\n' + 
 'execrecruiter' + '\n' + 
 'familyownedbusiness' + '\n' +
 'filmvideoproductioncompany' + '\n' +   
 'financialadviser' + '\n' + 
 'financialinstitution' + '\n' +  
 'fitnessrecreationcenter' + '\n' + 
 'franchiser' + '\n' +
 'gamingsupplierscasinooperator' + '\n' +
 'graphicdesigncompany' + '\n' +  
 'greenbuilder' + '\n' +
 'greenserviceprovider' + '\n' + 
 'hispanicmedia' + '\n' + 
 'hospital' + '\n' +
 'insurancebroker' + '\n' + 
 'itserviceprovider' + '\n' +
 'largestemployer' + '\n' + 
 'largestmanufacturer' + '\n' +
 'legalsupportservice' + '\n' + 
 'mediacompany' + '\n' + 
 'medicalgroup' + '\n' +
 'minoritymediacompany' + '\n' +
 'minorityownedbusiness' + '\n' +
 'mortgagelender' + '\n' +
 'nationalbank' + '\n' +
 'officefurniture' + '\n' + 
 'officemachine' + '\n' + 
 'optometrist' + '\n' +
 'payrollcompany' + '\n' +
 'physicaltherapy' + '\n' +
 'professionalorg' + '\n' +
 'publicrelations' + '\n' +
 'residentialhomebuilder' + '\n' +
 'residentialrebroker' + '\n' +
 'residentialtopsalesagent' + '\n' + 
 'sbalender' + '\n' +
 'specialtyclinic' + '\n' + 
 'staffingfirm' + '\n' +
 'stockbroker' + '\n' +
 'technology' + '\n' +
 'telecommunications' + '\n' +
 'transportationservice' + '\n' +
 'treatmentcenter' + '\n' +
 'urgentcarecenter' + '\n' +
 'venturecapitalfirm' + '\n' +
 'wastemanagementservice';

/*
 'wirelesscableprovider' + '\n' +
 'bankruptcyattorney' + '\n' +
 'buscommlitigationattorney' + '\n' +
 'criminalattorney' + '\n' +
 'gamingattorney' + '\n' +
 'generalpracticeattorney' + '\n' +
 'governmentaffairsattorney' + '\n' +
 'immigrationattorney' + '\n' +
 'intellectualpropertyattorney' + '\n' +
 'lawfirm' + '\n' +
 'litigationattorney' + '\n' +
 'locallawfirm' + '\n' +
 'medicalmalpracticeattorney' + '\n' + 
 'nationallawfirm' + '\n' +
 'personalinjuryattorney' + '\n' +
 'assistedlivingfacility' + '\n' +
 'chamberofcommerce' + '\n' +
 'charitableorganization' + '\n' +
 'citycountybusinessservice' + '\n' +
 'municipalbusinessservice' + '\n' +
 'industrialpark' + '\n' +
 'officepark' + '\n' +
 'laborunion' + '\n' +
 'college' + '\n' +
 'professionalcertification' + '\n' +
 'privateschool' + '\n' +
 'graduateprogram' + '\n' +
 'femalebusinessleader' + '\n' +
 'industryleader'  + '\n' +
 'largestofficeindustrial' + '\n' +
 'largestretail' + '\n' +
 'minoritybusinessleader' + '\n' +
 'networkinggroup' + '\n' +
 'pediatricgrouppractice' + '\n' +
 'restaurant' + '\n' +
 'shoppingcenter' + '\n' +
 'topbankpresident' + '\n' +
 'tradeassociation' + '\n' +
 'tvanchor'  + '\n' +
 'titlecompany' + '\n' +
 'pharmacy' + '\n' +
 'meetingfacility';

*/






function Schedule1_OnAction(me, eventInfo)
{
    var iSystemTime_s = Math.floor( Date.now());
    project.setTag("Codesys_HMI/Application/GVL/HMI/Datetime_UNIX", iSystemTime_s);
    
    
    iYear = new Date().getFullYear();
    iMonth = new Date().getMonth() + 1;
    iDay = new Date().getDate();
    iHour = new Date().getHours();
    iMin = new Date().getMinutes();
    iSecond = new Date().getSeconds();
    iMiliSec    = new Date().getMilliseconds();
    
    var sCurrentDateTime;
    
        
    sCurrentDateTime = iYear.toString();    
    sCurrentDateTime = sCurrentDateTime + ('0' +  iMonth.toString()).slice(-2);
    sCurrentDateTime = sCurrentDateTime + ('0' +  iDay.toString()).slice(-2);
        
    sCurrentDateTime = sCurrentDateTime + "_" + ('0' +  iHour.toString()).slice(-2);
    sCurrentDateTime = sCurrentDateTime + ('0' +  iMin.toString()).slice(-2);
    sCurrentDateTime = sCurrentDateTime + ('0' +  iSecond.toString()).slice(-2);
    sCurrentDateTime = sCurrentDateTime + "_" +('0000' +  iMiliSec.toString()).slice(-4);
    
    project.setTag("Codesys_HMI/Application/GVL/HMI/Datetime_String", sCurrentDateTime);
    
    return false; 
}
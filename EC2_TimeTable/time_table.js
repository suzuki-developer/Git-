function timeTable() {
    var nowTime = new Date();
    var nowYear = nowTime.getFullYear();
    var nowHour = nowTime.getHours();
    var nowMin  = nowTime.getMinutes();
    var nowSec  = nowTime.getSeconds();
    var msg     = "現在時刻は、" + nowYear + "年" + nowHour + "時" + nowMin + "分" + nowSec + "秒";

    document.getElementById("RealtimeClockArea").innerHTML = msg;
}

setInterval('timeTable()', 1000);

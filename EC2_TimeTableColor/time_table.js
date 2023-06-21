function timeTable() {
    var nowTime = new Date();
    var nowYear = nowTime.getFullYear();
    var nowHour = nowTime.getHours();
    var nowMin  = nowTime.getMinutes();
    var nowSec  = nowTime.getSeconds();
    var msg     = nowYear + "年" + nowHour + "時" + nowMin + "分" + nowSec + "秒";

    document.getElementById("RealtimeClockArea").innerHTML = msg;

    var clockColor = document.getElementById("RealtimeClockArea");
    if (nowSec % 2 == 0) {
        clockColor.classList.remove("blue");
        clockColor.classList.add("red");
    } else {
        clockColor.classList.remove("red");
        clockColor.classList.add("blue");
    }
}

setInterval('timeTable()', 1000);

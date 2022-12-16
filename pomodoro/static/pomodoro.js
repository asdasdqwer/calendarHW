let root = document.querySelector(":root");
let paragraph = document.getElementById("time");
var button = document.getElementById("start");
var started = false;
let fill, countdown;

button.onclick = function() {
    if (!started) {
        started = true;
        this.innerHTML = "Stop";
        var start = Date.now();
        let length = 0;

        fill = setInterval(function() {
            root.style.setProperty('--length', length.toString() + "px");
            length++;
        }, 100);

        countDown = setInterval(function() {
            var delta = Math.round((1500000 - Date.now() + start) / 1000);
            paragraph.innerHTML = Math.floor(delta / 60).toString() + ":" + (delta % 60).toString();
        }, 1000);
    }
    
    else {
        this.innerHTML = "Start";
        started = false;
        clearInterval(countDown);
        clearInterval(fill);
        length = 0;
        root.style.setProperty('--length', length.toString() + "px");
        paragraph.innerHTML = "25:00";
        
    }
}

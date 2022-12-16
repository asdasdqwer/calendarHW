//set date to today's date

//document.getElementById("inputDate").valueAsDate = new Date();

var darkmode = document.getElementById("darkmode").textContent.toLowerCase();

if (darkmode == "true") {
        darkmode = true;
}

else {
        darkmode = false;
}

if (darkmode) {
        var root = document.querySelector(":root");
        root.style.setProperty('--backgroundColor', '#212124');
        root.style.setProperty('--fieldBackground', '#323232');
        root.style.setProperty('--fontColor', '#FFF');
}

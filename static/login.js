//Set width and height to a fixed value

function getCookie(cname) {
	let name = cname + "=";
	let ca = document.cookie.split(';');
	for(let i = 0; i < ca.length; i++) {
		let c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return "";
}

var darkmode = document.getElementById("darkmode");


if (darkmode == "True") {
        darkmode = true;
}

else {
        darkmode = false;
}

if (darkmode) {
        let root = document.querySelector(":root");
        root.style.setProperty('--backgroundColor', '#363062');
        root.style.setProperty('--fieldBackground', '#4D4C7D');
        root.style.setProperty('--buttonFont', '#000');
        root.style.setProperty('--buttonFontHover', '#FFF');
        root.style.setProperty('--buttonBG', '#C1C1C1');
        root.style.setProperty('--buttonBGOnHover', '#12113');
}



var button = document.getElementsByTagName("button")[0];


const arr = [document.getElementsByTagName("button")[0],
             document.getElementById("username"),
             document.getElementById("password"),
             document.getElementById("all")
            ]

for (var i = 0; i < 4; i++) {
/*	if (getCookie("height_" + arr[i].id) != "") {
		arr[i].style.height = getCookie("height_" + arr[i].id);
		arr[i].style.width = getCookie("width_" + arr[i].id);
	}

	else {
*/	arr[i].style.height = arr[i].offsetHeight.toString() + "px";
	arr[i].style.width = arr[i].offsetWidth.toString() + "px";
//		document.cookie += "height_" + arr[i].id + "=" + arr[i].style.height.toString() + ";";
//		console.log("height_" + arr[i].id + "=" + arr[i].style.height.toString() + ";");
//		document.cookie += "width_" + arr[i].id + "=" + arr[i].style.width.toString() + ";";
}

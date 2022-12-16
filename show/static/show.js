//set date to today's date

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

function detectURLs(message) {
	var urlRegex = /(((https?:\/\/)|(www\.))[^\s]+)/g;
	return message.match(urlRegex);
}

var textarea = document.getElementById("task");
var content = textarea.innerHTML.replaceAll("\n", "<br>");
document.getElementById("task").innerHTML = content;
var urls = detectURLs(content);

if (urls.length != 0) {
	for (var i = 0; i < urls.length; i++) {
		content = content.split(urls[i]).join("<a href=\"" + urls[i] + "\"> " + urls[i] + " </a>");
	}
}

document.getElementById("task").innerHTML = content;

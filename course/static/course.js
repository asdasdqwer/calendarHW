var categories = JSON.parse(JSON.parse(document.getElementById("subjectClasses").textContent));
var subjects = JSON.parse(JSON.parse(document.getElementById("subjects").textContent));
var subjectsFlattened = subjects.flat();

var courses = JSON.parse(JSON.parse(document.getElementById("availableCourses").textContent));

var alreadySelectedCourses = JSON.parse(JSON.parse(document.getElementById("selectedCourses").textContent));

var heightPos;

var classes = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"];

// add short forms to categories
var temp = [];
for (var i = 0; i < categories.length; i++) {
	if (categories[i] == "Gesellschaftswissenschaften" && screen.height > screen.width) {
		categories[i] = "Gesellschafts-<br>wissenschaften";
	}
        var counter = 2;
        while (temp.includes(categories[i].substring(0, counter))) {
                counter++;
        }

        temp.push(categories[i].substring(0, counter));

        categories[i] = [categories[i], categories[i].substring(0, counter).toLowerCase()];
}
// generate short forms of subjects and selected array

var temp = [];
var subjectsShort = [];
var selected = [];
for (var i = 0; i < subjects.length; i++) {
	selected.push([]);
	subjectsShort.push([]);
	for (var j = 0; j < subjects[i].length; j++) {
		subjectsShort[i].push([]);
		selected[i].push([]);
	        var counter = 2;
        	while (temp.includes(subjects[i][j].substring(0, counter))) {
                	counter++;
	        }

        	temp.push(subjects[i][j].substring(0, counter));

	        subjectsShort[i][j] = [subjects[i][j].substring(0, counter)];
	}
}
//darkmode
var darkmode = document.getElementById("darkmode").textContent.toLowerCase();

if (darkmode == "true") {
        darkmode = true;
        var root = document.querySelector(":root");
        root.style.setProperty('--backgroundColor', '#212124');
        root.style.setProperty('--fieldBackground', '#323232');
        root.style.setProperty('--buttonFontHover', '#FFF');
        root.style.setProperty('--buttonBGOnHover', '#12113');
        root.style.setProperty('--invertPercentage', '100%');
}

else {
    darkmode = false;
}
// set go back function

let img = document.getElementById("back");

img.onclick = function() {

    var submitButton = document.getElementById("submit");
    submitButton.style.visibility = "visible";
    submitButton.style.display = "flex";

    var allElements = document.getElementsByClassName("subjects");
    for (var m = 0; m < allElements.length; m++) {
        allElements[m].style.visibility = "visible";
        allElements[m].style.display = "block";
    }

    var allHeaders = document.getElementsByTagName("h1");

    for (var m = 0; m < allHeaders.length; m++) {
        allHeaders[m].style.visibility = "visible";
        allHeaders[m].style.display = "block";
    }

    var allElements = document.getElementsByClassName("courses");
    for(var m = 0; m < allElements.length; m++) {
        allElements[m].style.visibility = "hidden";
        allElements[m].style.display = "none";
    }

    img.style.visibility = "hidden";
    img.style.display = "none";
    window.scrollTo(0, heightPos); // Scroll back where user was before
};

for (let i = 0; i < subjects.length; i++) {
    var h1 = document.createElement("h1");
    h1.innerHTML = categories[i][0];

    document.body.appendChild(h1);

    for (let j = 0; j < subjects[i].length; j++) {
        let div = document.createElement("div");
        div.className = "subjects " + categories[i][1] + " " + classes[i];
        div.id = subjectsShort[i][j];
        div.innerHTML = "<h3>" + subjects[i][j] + "</h3>";
        div.onclick = function () {
            heightPos = window.scrollY;
            img.style.visibility = "visible";
            img.style.display = "block";

            var submitButton = document.getElementById("submit");
            submitButton.style.visibility = "hidden";
            submitButton.style.display = "none";

            var allElements = document.getElementsByClassName("subjects");
            for (var m = 0; m < allElements.length; m++) {
                allElements[m].style.visibility = "hidden";
                allElements[m].style.display = "none";
            }

            var allHeaders = document.getElementsByTagName("h1");

            for (var m = 0; m < allHeaders.length; m++) {
                allHeaders[m].style.visibility = "hidden";
                allHeaders[m].style.display = "none";
            }

            var allElements = document.getElementsByClassName(subjectsShort[i][j]);
            for(var m = 0; m < allElements.length; m++) {
                allElements[m].style.visibility = "visible";
                allElements[m].style.display = "block";
            }
        };
        document.body.appendChild(div);
        for (let k = 0; k < courses[i][j].length; k++){
            let div2 = document.createElement("div");
            div2.className = subjectsShort[i][j] + " courses " + categories[i][1] + " " + classes[i];
            div2.id = subjectsShort[i][j] + k.toString();
            let selectedCourseName = courses[i][j][k];
            div2.innerHTML = "<h3>" + selectedCourseName + "</h3>";

            div2.onclick = function() {
                var currentTeacher = selected[i][j][0];
                if (currentTeacher == selectedCourseName) { //Unselect current course
                    selected[i][j] = [];
                    div2.lastChild.remove();
                    div.lastChild.remove();
                    return;
                }

                var tickImg = document.createElement("img");
                tickImg.src = "/media/tick.png";
                tickImg.className = "tickImg";
                div2.appendChild(tickImg);
                div.appendChild(tickImg.cloneNode(true));

                if (selected[i][j].length == 0) {
                    selected[i][j].push(selectedCourseName);
                }

                else {
                    var selectedDiv = document.getElementById(subjectsShort[i][j] + courses[i][j].indexOf(currentTeacher).toString());
                    //SubjectsShort[i][j] for the subject name, e.g. "de", "e5" etc.
                    //courses[i][j]... for getting the following number corresponding to the div that is currently selected / has the green border

                    selectedDiv.lastChild.remove();
                    div.lastChild.remove();

                    selected[i][j][0] = selectedCourseName;
                }


            };

            if (alreadySelectedCourses.includes(selectedCourseName)) {
                div2.click();
            }

            document.body.appendChild(div2);
        }
    }
}

var submit = document.createElement("div");
submit.id = "submit";
submit.innerText = "Senden";
submit.onclick = function() {
    selectedFlattened = selected.flat().flat();

    if (selectedFlattened.length == 0) {
        alert("Wählen sie bitte Ihre Kurse aus");
        return;
    }

    for (var iterator = 0; iterator < selectedFlattened.length; iterator++) {
        if (selectedFlattened[iterator].indexOf(" (") != -1)
            selectedFlattened[iterator] = selectedFlattened[iterator].slice(0, selectedFlattened[iterator].indexOf(" ("));
            //Remove teachers name
    }

    $.ajax({
        type: "POST",
        url: "",

        data: {
            selectedFlattened: JSON.stringify(selectedFlattened),
            csrfmiddlewaretoken: window.CSRF_TOKEN
        },

        success: function(html) {
            window.open("/homework", "_self");
        }
    });
};

document.body.appendChild(submit);


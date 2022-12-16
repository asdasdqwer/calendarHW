var d = new Date();
var days = ["Mo", "Di", "Mi", "Do", "Fr"];
var months = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"];
var currentDay = d.getDay(); //Get the day of the week, eg. monday, .... as number
var monthDay = d.getDate(); //Get the day of the month, eg. 16th December --> 16
var dates = [[], []];
if (currentDay == 6) {
	currentDay = -1; // for saturdays to be set to next week
}

var taskList = JSON.parse(JSON.parse(document.getElementById("task").textContent));
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
	root.style.setProperty('--finishedFont', '#C1C1C1');
	root.style.setProperty('--invertPercentage', '100%');
	root.style.setProperty('--activeBG', '#449DD1');
	var DMLink = document.getElementById("darkmodeLink");
	DMLink.innerHTML = "Lightmode";
}




//Set Day to first day of the week
d.setDate(d.getDate() - currentDay + 1);

//set day to first day of two weeks ago

d.setDate(d.getDate() - 14);

function changeCheckBox() {
    var $link = $(this).parent().parent().children(".taskTitleBox").children("a")[0];
    if ($link.className.includes("finished")) {
        $link.className = $link.className.replace("finished", "notFinished");
    }

    else {
        $link.className = $link.className.replace("notFinished", "finished");
    }

    $.ajax({
        type: "POST",
        url: "",

        data: {
            task: $link.id,
            csrfmiddlewaretoken: window.CSRF_TOKEN 
        },
    });
}

var list;
async function createTaskListForDay() {
	//set background color
	$(".activeDay").removeClass("activeDay");
	this.className = this.className + " activeDay";

	// check if task list already exists
	var pDate = this.id.split("/").join("-");

	var tempTaskList = document.getElementById("taskList" + pDate);

	$(".taskList").css("display", "none");
	$(".taskList").css("visibility", "hidden");

	if (tempTaskList) {
		$("#" + "taskList" + pDate).css("display", "block");
		$("#" + "taskList" + pDate).css("visibility", "visible");
	}

	else {
		await $.ajax({
			type: "GET",
			url: "",

			data: {
				date: pDate
			},

			success: function(res) {
				list = JSON.parse(res["taskList"]);
			}
		});

		var taskListForDay = document.createElement("div");
		taskListForDay.id = "taskList" + pDate;
		taskListForDay.className = "taskList";
		for (arr of list) {
			taskListForDay.appendChild(createTaskBox(arr[0], arr[1], arr[2]));
		}

		document.body.appendChild(taskListForDay);
		$("#" + "taskList" + pDate).css("display", "block");
		$("#" + "taskList" + pDate).css("visibility", "visible");
		
		setTimeout(function () {
			$(".animation").removeClass("animation");
		}, 500);
	}

}

function createWeek(startDate) {
	var weekDiv = document.createElement("div");
	weekDiv.className = "week";

	for (var i = 0; i < 5; i++) {
		var dayDiv = document.createElement("div");
		if (i == 0) {
			dayDiv.className = "days firstDay";
		}

		else if (i == 5) {
			dayDiv.className = "days lastDay";
		}

		else {
			dayDiv.className = "days";
		}

		dayDiv.id = startDate.toLocaleDateString("en-us",{"year": "numeric", "month": "numeric", "day":"numeric"});
		dayDiv.onclick = createTaskListForDay;

		var p1 = document.createElement("p");
		var p2 = document.createElement("p");
		var p3 = document.createElement("p");
		p1.className = "dayName";
		p2.className = "monthName";
		p3.className = "dateName";
		p1.innerHTML = days[i];
		p2.innerHTML = months[startDate.getMonth()];
		p3.innerHTML = startDate.getDate().toString();
		dayDiv.appendChild(p1);
		dayDiv.appendChild(p2);
		dayDiv.appendChild(p3);
		weekDiv.appendChild(dayDiv);
		startDate.setDate(startDate.getDate() + 1);
	}

	return weekDiv;
}



function createTaskBox(title, id, finished) {
	finished = !!finished;
	var taskBox = document.createElement("div");
	taskBox.className = "taskBox animation";

	var boxForCheckBox = document.createElement("div");
	boxForCheckBox.className = "boxForCheckBox";

	var checkBox = document.createElement("input");
	checkBox.setAttribute("type", "checkbox");
	checkBox.className = "checkbox";
	checkBox.checked = finished;
	checkBox.onclick = changeCheckBox;

	var taskTitleBox = document.createElement("div");
	taskTitleBox.className = "taskTitleBox";
	taskTitleBox.onclick = function () {
		this.firstChild.click();
	}

	var taskTitle = document.createElement("a");
	taskTitle.className = "taskTitle";
	taskTitle.id = id.toString();
	taskTitle.innerHTML = title;
	taskTitle.href = "/show/" + id.toString();

	if (finished) {
		taskTitle.className = taskTitle.className + " finished";
	}

	else {
		taskTitle.className = taskTitle.className + " notFinished";
	}

	boxForCheckBox.appendChild(checkBox);
	taskTitleBox.appendChild(taskTitle);

	taskBox.appendChild(boxForCheckBox);
	taskBox.appendChild(taskTitleBox);

	return taskBox;
}

function addBoxesToDays() {
	if (this.scrollLeft === 0){
		var firstDate = new Date(this.firstChild.firstChild.id);

		firstDate.setDate(firstDate.getDate() - 7);

		$(this).prepend(createWeek(firstDate));

		$(this).scrollLeft(this.offsetWidth);

		return;
	}

	if (this.scrollLeft === (this.offsetWidth * (this.childElementCount - 1))) {
		var posBeginning = this.scrollLeft;

		var lastDate = new Date(this.lastChild.lastChild.id);

		lastDate.setDate(lastDate.getDate() + 3);

		this.appendChild(createWeek(lastDate));

		$(this).scrollLeft(posBeginning);
	}
}



var daysSelect = document.getElementById("daysSelect");
daysSelect.onscroll = addBoxesToDays;
for (var i = 0; i < 5; i++) {
	daysSelect.appendChild(createWeek(d));
	d.setDate(d.getDate() + 2);
}

// scroll to actual date
$(daysSelect).scrollLeft((window.innerWidth)*2);

function clickCurrentDate() {
	// get date of next day, then click on it
	var d = new Date();

	// for saturdays and sundays
	d.setDate(d.getDate() + 1);
	while ((d.getDay() == 6) || (d.getDay() == 0)) {
		d.setDate(d.getDate() + 1);
	}

	var dayElement = document.getElementById(d.toLocaleDateString("en-us",{"year": "numeric", "month": "numeric", "day":"numeric"}));
	dayElement.click()
}

clickCurrentDate();






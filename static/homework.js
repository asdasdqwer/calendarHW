var d = new Date();
var days = [0, "Mon", "Tue", "Wed", "Thu", "Fri"];
var currentDay = d.getDay(); //Get the day of the week, eg. monday, .... as number
var monthDay = d.getDate(); //Get the day of the month, eg. 16th December --> 16
var dates = [[], []];
/*if ((currentDay >= 6) || (currentDay == 5 && d.getHours() >= 17)){
    currentDay = 7;
};*/

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
	root.style.setProperty('--invertPercentage', '100%');
	var DMLink = document.getElementById("darkmodeLink");
	DMLink.innerHTML = "Lightmode";
}


//Set Day to first day of the week
d.setDate(d.getDate() - currentDay + 1);

function changeCheckBox() {
    var $link = $(this).parent().parent().children("a")[0];
    console.log($link.className);
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
            task: this.id,
            csrfmiddlewaretoken: window.CSRF_TOKEN 
        },
    });
}
for(var i = 1; i <= 2; i++) {
    for (var j = 1; j <= 5; j++) {
        var div1 = document.createElement("div");
        div1.id = days[j].toLowerCase() + i.toString() + "LeftDiv";
        div1.className = "leftDiv";
        var div2 = document.createElement("div");
        div2.id = days[j].toLowerCase() + i.toString() + "RightDiv";
        div2.className = "rightDiv";
        
        var day = document.getElementById(days[j].toLowerCase() + i.toString());
        var p1 = document.createElement("p");
        var p2 = document.createElement("p");
        var br = document.createElement("br");
        p1.innerHTML = days[j].toString();
        p2.innerHTML = d.getDate().toString();
        
        if (d.getDate() == monthDay) {
            p1.style.color = "orange";
            //p2.style = "border-radius: 50%; background-color: orange;"
            p2.style.color = "orange";
            

        }
        p1.className = "dayName";
        p2.className = "dayNumber";
        d.setDate(d.getDate() + 1); //Next day
        div1.appendChild(p1);
        div1.appendChild(br);
        div1.appendChild(p2);
        day.appendChild(div1);
        
        for (var k = 0; k < taskList[i-1][j-1].length; k++) {
            var tempDiv = document.createElement("div"); // For flexbox reasons
            tempDiv.className = "box";
            /*if (k == 3) {
                break;
            }*/
            
            var pLeft = document.createElement("a");
            pLeft.innerHTML = taskList[i-1][j-1][k][0];
            pLeft.className = "singleTask";
            if (k == (taskList[i-1][j-1].length - 1)) {
                pLeft.className = "singleTask lastTask";
            }
            
            pLeft.setAttribute('href', '/show/' + taskList[i-1][j-1][k][1].toString());
            var boxForCheckBox = document.createElement("div");
            boxForCheckBox.className = "boxForCheckBox";
            
            var checkBox = document.createElement("input");
            checkBox.type = "checkbox";
            checkBox.className = "checkBox";
            checkBox.id = taskList[i-1][j-1][k][1].toString();
            checkBox.checked = !!taskList[i-1][j-1][k][2]; // converts 0/1 to boolean
            if (checkBox.checked) {
                pLeft.className = pLeft.className + " finished";
            }
            
            else {
                pLeft.className = pLeft.className + " notFinished";
            }
            checkBox.onclick = changeCheckBox;
            boxForCheckBox.appendChild(checkBox);
            tempDiv.appendChild(boxForCheckBox);
            tempDiv.appendChild(pLeft);
            div2.appendChild(tempDiv);
        }
        day.appendChild(div2);
    }

    d.setDate(d.getDate() + 2);
}


$(".lastTask").parents('.box').css("margin-bottom", "10px");

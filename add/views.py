from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from login.models import Task, Course, CheckBox

def createCheckBoxes(pTask):
    allUsers = pTask.course.user.all()
    for i in allUsers:
        checkbox = CheckBox.objects.create(checked=False, user=i, task=pTask)
        checkbox.save()
    del(allUsers)

@login_required
@permission_required("login.add_task", login_url="")
def addTask(request):
    user = User.objects.get(username=request.user.username)

    if request.method == "POST":
        taskTypesShort = {
            "Hausaufgabe": "HA",
            "Klausur (mit Test)": "KT",
            "Klausur (ohne Test)": "KL",
            "Test": "TS"
        }

        title = request.POST["title"]
        taskType = taskTypesShort[request.POST["taskType"]]

        if request.POST["description"] == "":
            raise Http404

        if title == "":
            taskTypesTitle = {"HA": "HA", "KT": "Klausur", "KL": "Klausur", "TS": "Test"}
            title = " ".join((request.POST["subject"], taskTypesTitle[taskType]))
            del(taskTypesTitle)
            

        task = Task(
            taskTitle=title,
            finishDate=datetime.strptime(request.POST["inputDate"], '%Y-%m-%d').date(),
            taskDescription=request.POST["description"],
            taskType=taskType,
            course=Course.objects.get(subjectName__subjectName=request.POST["subject"], user=user),
            user=user
        )
        task.save()
        
        createCheckBoxes(task)
        
        a = open(str(settings.BASE_DIR.parent.joinpath("add.txt")), "a")
        a.write(" ".join((request.user.username, str(datetime.now()), str(task.id), "\n")))
        a.close()
        
        del(title, taskType, taskTypesShort, user, task)
        return redirect("/homework")
    subjects = [str(i.subjectName) for i in user.courses.all()]
    context = {
        "subjects": subjects,
        "darkmode": user.student_user.darkModeEnabled
    }

    del(subjects, user)
    return render(request, "add.html", context)

from datetime import date, timedelta, datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from json import dumps
import os
from login.models import Task, CheckBox

@login_required
def calendarRender(request):
    if request.method == "POST":
        checkBox = CheckBox.objects.get(task=Task.objects.get(id=int(request.POST["task"])), user=User.objects.get(username=request.user.username))
        checkBox.checked = not checkBox.checked
        checkBox.save()
        del(checkBox)
        return JsonResponse({'success': True}, status=200)

    if request.GET:
        selectedDate = datetime.strptime(request.GET["date"], "%m-%d-%Y")
        u = User.objects.get(username=request.user.username)
        coursesFromUser = [i.courseName for i in u.courses.all()]
        taskList = [[k.taskTitle, k.id, int(k.checkbox_task.get(user=u))] for k in Task.objects.filter(course__courseName__in=coursesFromUser, course__grade=u.student_user.grade, finishDate=selectedDate)]
        context = {
            "taskList": dumps(taskList)
        }

        del(taskList, coursesFromUser, u, selectedDate)
        return JsonResponse(context)

    a = open("".join((os.getenv("HOME"), "/log.txt")), "a")
    a.write(" ".join((request.user.username, str(datetime.now()), "view calendar mobile\n")))
    a.close()
    u = User.objects.get(username=request.user.username)
    coursesFromUser = [i.courseName for i in u.courses.all()]
    if len(coursesFromUser) == 0: # if user hasn't selected any courses yet
        del(coursesFromUser)
        return redirect("/course/")
    tomorrow = date.today() + timedelta(days=1)
    taskList = [[k.taskTitle, k.id, int(k.checkbox_task.get(user=u))] for k in Task.objects.filter(course__courseName__in=coursesFromUser, course__grade=u.student_user.grade, finishDate=tomorrow)]
    del(tomorrow)
    context = {
        "taskList": dumps(taskList),
        "darkmode": u.student_user.darkModeEnabled
    }
    del(taskList, coursesFromUser, u)
    return render(request, "homework_mobile.html", context)

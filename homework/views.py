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

    a = open("".join((os.getenv("HOME"), "/log.txt")), "a")
    a.write(" ".join((request.user.username, str(datetime.now()), "view calendar\n")))
    a.close()
    u = User.objects.get(username=request.user.username)
    coursesFromUser = [i.courseName for i in u.courses.all()]
    if len(coursesFromUser) == 0: # if user hasn't selected any courses yet 
        del(coursesFromUser)
        return redirect("/course/")
    start = date.today() - timedelta(days=date.today().weekday() if date.today().weekday() != 6 else -1)
    temp = Task.objects.filter(course__courseName__in=coursesFromUser, course__grade=u.student_user.grade)
    task = [[[[k.taskTitle, k.id, int(k.checkbox_task.get(user=u))] for k in temp.filter(finishDate=start+timedelta(days=i+7*j))] for i in range(5)] for j in range(2)]
    del(start, temp)
    context = {
        "taskList": dumps(task),
        "darkmode": u.student_user.darkModeEnabled
    }
    del(task, coursesFromUser, u)
    return render(request, "homework.html", context)

"""for u in User.objects.all():
    coursesFromUser = [i.courseName for i in u.courses.all()]
    if len(coursesFromUser) != 0:
        for t in Task.objects.filter(course__courseName__in=coursesFromUser, course__grade=u.student_user.grade):
            c = CheckBox.objects.create(task=t, user=u, checked=False)
            c.save()"""
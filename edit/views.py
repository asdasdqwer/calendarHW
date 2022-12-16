from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404
from login.models import Task, Course, CheckBox
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required

def changeCheckBox(pTask, newcourse):
    allUsersOfOldCourse = pTask.course.user.all()
    
    for i in allUsersOfOldCourse:
        checkbox = CheckBox.objects.get(user=i, task=pTask)
        checkbox.delete()
    del(allUsersOfOldCourse)
    
    allUsersOfNewCourse = newcourse.user.all()
    
    for i in allUsersOfNewCourse:
        checkbox = CheckBox.objects.create(checked=False, user=i, task=pTask)
        checkbox.save()
    del(allUsersOfNewCourse)
    
@login_required
@permission_required("login.add_task", login_url="")
def editTask(request, id):
    user = User.objects.get(username=request.user.username)
    task = Task.objects.get(id=id)
    course = task.course
    if course not in user.courses.all():
        raise Http404("Aufgabe mit dieser Id existiert nicht")


    if request.method == "POST":
        if request.POST["title"] != "":
            task.taskTitle = request.POST["title"]
        newCourse = Course.objects.get(
                    subjectName__subjectName=request.POST["subject"],
                    user=user)
        if task.course != newCourse:
            changeCheckBox(task, newCourse)
            task.course = newCourse
        task.finishDate = datetime.strptime(request.POST["inputDate"], '%Y-%m-%d').date()
        task.taskType = request.POST["taskType"]
        task.taskDescription = request.POST["description"]
        task.user = user

        task.save()
#        a = open("/home/erv/calendarHW/edit/edit.txt", "a")
#        a.write(" ".join((user.username, str(datetime.now()), str(task.id), str(task.finishDate), task.taskType, task.taskDescription, str(task.course), "\n")))
#        a.close()
        #['taskTitle, finishDate', 'taskType', 'taskDescription', 'course']
        del(task, user)
        return redirect("/homework/")

    subjectName = task.course.subjectName.subjectName
    subjects = [str(i.subjectName) for i in user.courses.all()]
    subjects.remove(subjectName)
    subjects.insert(0, subjectName)

    context = {
        "subjects": subjects,
        "title": task.taskTitle,
        "finishDate": str(task.finishDate),
        "description": task.taskDescription,
        "taskType": task.get_taskType_display(),
        "darkmode": user.student_user.darkModeEnabled
    }

    del(subjectName, subjects, task, user, course)

    return render(request, "edit.html", context)

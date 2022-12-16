from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from login.models import Task


@login_required
def showTask(request, id):
#    a = open("/home/erv/log.txt", "a")
#    a.write(" ".join((request.user.username, str(datetime.now()), "show", str(id), "\n")))
#    a.close()

    try:
        task = Task.objects.get(id=id)
    except:
        raise Http404("Aufgabe nicht gefunden")
    user = User.objects.get(username=request.user.username)

    if task.course not in user.courses.all():
        raise Http404("Aufgabe nicht gefunden")

#    user = User.objects.get(username=request.user.username)
#    coursesFromUser = [str(i) for i in User.objects.get(username=request.user.username).courses.all()]
    if str(task.course) not in [str(i) for i in user.courses.all()]:
        raise Http404()
#    del(coursesFromUser)

    context = {
        "task": [task.taskTitle, ".".join(str(task.finishDate).split("-")[::-1]), str(task.course.subjectName), task.get_taskType_display(), task.taskDescription, request.user.has_perm('homework.add_task')],
        "darkmode": user.student_user.darkModeEnabled
    }

    return render(request, "show.html", context)

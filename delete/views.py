from django.shortcuts import redirect
from django.http import Http404
from login.models import Task, CheckBox
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

def deleteCheckBox(pTask):
    allUsers = pTask.course.user.all()
    
    for i in allUsers:
        checkbox = CheckBox.objects.get(user=i, task=pTask)
        checkbox.delete()
    del(allUsers)

@login_required
@permission_required("login.add_task")
def deleteTask(request, id):
    task = Task.objects.get(id=id)
    course = task.course
    if course not in User.objects.get(username=request.user.username).courses.all():
        raise Http404("Beim Löschen dieser Aufgabe ist etwas schiefgelaufen")
#    a = open("/home/erv/calendarHW/delete/delete.txt", "a")
#    a.write(" ".join((request.user.username, str(datetime.now()), str(task.finishDate), task.taskType, task.taskDescription, str(task.course), "\n")))
#    a.close()
    deleteCheckBox(task)
    task.delete()
    del(task)
    return redirect("/homework")

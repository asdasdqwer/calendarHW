from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.models import Student, School, Grade
from datetime import datetime

@login_required
def stufeView(request):
    a = open("/home/erv/log.txt", "a")
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        try:
            student = Student.objects.create(school=School.objects.all()[0], grade=Grade.objects.get(grade=int(request.POST["stufe"])), user=user)
            student.save()
        except:
            student = Student.objects.get(user=user)
            student.grade = Grade.objects.get(grade=int(request.POST["stufe"]))
            student.save()
        a.write(request.user.username + " " + str(datetime.now()) + " select stufe post\n")
        a.close()
        return redirect("/homework/")
    try:
        Student.objects.get(user=user)
        a.write(request.user.username + " " + str(datetime.now()) + " select stufe redirect\n")
        a.close()
        return redirect("/homework/")
    except:
        a.write(request.user.username + " " + str(datetime.now()) + " select stufe\n")
        a.close()
        return render(request, "stufe.html")

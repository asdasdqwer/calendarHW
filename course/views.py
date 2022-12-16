from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from json import dumps, loads
from datetime import datetime
from login.models import Course, SubjectClass, Subject, Student, CheckBox

def deleteCheckBoxes(pUser):
    for i in pUser.courses.all():
        for j in i.courses.all():
            CheckBox.objects.get(user=pUser, task=j).delete()

def createCheckBoxes(pUser):
    for i in pUser.courses.all():
        for j in i.courses.all():  #tasks
            c = CheckBox.objects.create(user=pUser, task=j, checked=False)
            c.save()

@login_required
def index(request):
    a = open("/home/erv/log.txt", "a")
    user = User.objects.get(username=request.user.username)

    if request.method == "POST":
        a.write(request.user.username + " " + str(datetime.now()) + " select course post\n")
        a.close()
        
        selected = loads(request.POST["selectedFlattened"])
        deleteCheckBoxes(user)
        user.courses.clear()
        for i in selected:
            course = Course.objects.get(courseName=i, school=user.student_user.school, grade=user.student_user.grade)
            user.courses.add(course)
        createCheckBoxes(user)
        del(user, selected, course)

        return redirect("/homework/")
    try:
        student = Student.objects.get(user=user)
    except:
        a.write(request.user.username + " " + str(datetime.now()) + " select course redirect stufe\n")
        a.close()
        return redirect("/stufe/")
    a.write(request.user.username + " " + str(datetime.now()) + " select course\n")
    a.close()
    subjectClasses = SubjectClass.objects.filter(school=user.student_user.school, grade=user.student_user.grade)
    s = Subject.objects.filter(school=user.student_user.school, grade=user.student_user.grade)
    subjects = [[str(j) for j in s.filter(subjectClass=i)] for i in subjectClasses]
    subjectClassesStr = [str(i) for i in subjectClasses]
    del(s, subjectClasses)
    availableCourses = [[] for i in range(len(subjectClassesStr))]
    selectedCourses = [str(i) for i in user.courses.all()]

    for i, j in enumerate(subjects):
        for k in j:
            availableCourses[i].append([str(l) for l in Course.objects.filter(subjectName__subjectName=k, grade=user.student_user.grade)])
    # Generate all courses existing in the database

    context = {
        "availableCourses": dumps(availableCourses),
        "selectedCourses": dumps(selectedCourses),
        "subjectClasses": dumps(subjectClassesStr),
        "subjects": dumps(subjects),
        "darkmode": user.student_user.darkModeEnabled
    }

    del(subjectClassesStr, subjects, user)

    return render(request, "course.html", context)

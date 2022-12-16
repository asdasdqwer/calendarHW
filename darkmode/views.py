from django.shortcuts import redirect
from login.models import Student
from django.contrib.auth.models import User
# Create your views here.

def changeView(request):
	u = Student.objects.get(user=User.objects.get(username=request.user.username))
	u.darkModeEnabled = not u.darkModeEnabled
	u.save()
	return redirect("/homework/")

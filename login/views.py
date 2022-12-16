from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Permission

def loginInterface(request):
    context = {
        "msg": ""
    }
    
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if len(user.courses.all()) == 0:
            return redirect("/stufe/")
        else:
            return redirect("/homework/")

    if request.method == "POST":
        username = request.POST["username"].lower().replace(" ", "")
        password = request.POST["password"]
        a = open("/home/erv/log.txt", "a")
        a.write(username + " " + str(datetime.now()) + " login\n")
        a.close()
        try:
            userToSetPassword = User.objects.get(username=username)
            if not userToSetPassword.has_usable_password():
                userToSetPassword.set_password(password)
                userToSetPassword.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("/course/")
            elif len(userToSetPassword.courses.all()) == 0:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/stufe/")
                else:
                    return render(request, "login.html", {"msg": "Benutzername oder Passwort falsch"})
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/homework/")
                else:
                    return render(request, "login.html", {"msg": "Benutzername oder Passwort falsch"})
        except:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/homework/")
        elif "." in username:
            user = User.objects.create_user(username=username, password=password)
            user.user_permissions.add(Permission.objects.get(name="Can add task"))
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("/stufe/")
        context = {
            "msg": "Benutzername oder Passwort falsch"
        }
    return render(request, "login.html", context)

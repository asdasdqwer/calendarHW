from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_user(request):
#    a = open("/home/erv/log.txt", "a")
#    a.write(" ".join((request.user.username, str(datetime.now()), "logout\n")))
#    a.close()
    logout(request)
    return redirect("/")

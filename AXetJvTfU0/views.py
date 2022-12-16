from django.shortcuts import redirect
from datetime import datetime
import os

def rickroll(request):
    a = open("".join((os.getenv("HOME"), "/rickroll.txt")), "a")
    a.write(" ".join((request.user.username, str(datetime.now()), "got rickrolled\n")))
    a.close()
    return redirect("https://www.youtube.com/watch?v=-AXetJvTfU0")

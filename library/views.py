import random

from django.contrib.auth.models import User
from django.http import HttpResponse


def index(request):
    res = HttpResponse("Hello, World!")
    nameList = ["Islam", "Muhammad", "Mesha", "Soad", "Sameh", "Wael"]
    res.write("<h1>" + nameList[random.randint(0, len(nameList)) - 1] + "</h1>")
    res.set_cookie('user_name', "Islam Mesha")
    return res


def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    # request.is
    return HttpResponse({}, user)

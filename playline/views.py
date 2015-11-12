from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import render
from school.models import Life

def home(request):
    lifes = Life.objects.all()[:10]
    return render(request,'playline/home.html',{"lifes": lifes})

def user(request,id):
    if request.user.is_authenticated():
        lifes = Life.objects.filter(user_id=id)
        accept_lifes = Life.objects.filter(accept_id=id)
        return render(request,'playline/user.html',{"lifes": lifes,'accept_lifes':accept_lifes})
    else:
        return render(request, 'school/login.html')

def about(request):
    return render(request,'playline/about.html')

def error(request):
    return render(request,'playline/error.html')
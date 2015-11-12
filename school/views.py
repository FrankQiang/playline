from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.models import Life
from .forms import LifeForm
from django.utils import timezone
from django.contrib.auth.models import User
#datetime.date.today()

# Create your views here.
def index(request):
    lifes = Life.objects.all()[:10]
    return render(request,'school/index.html',{"lifes": lifes})

def new(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = LifeForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                life_type_choices = form.cleaned_data['life_type_choices']
                info = form.cleaned_data['info']
                pub_date = timezone.now()
                user = User.objects.get(username=request.user.username)
                life = Life(pub_date=pub_date,title=title, info=info,life_type_choices=life_type_choices,watch=0,like=0,image='/static/img/example.jpg',expired=0,accept=0,user=user,accept_id=0)
                life.save()
                return HttpResponseRedirect('/')
        else:
            form = LifeForm()
        return render(request, 'school/new.html', {'form': form})
    else:
        return render(request, 'school/login.html')


def show(request,id):
    lifes = Life.objects.filter(id=id,expired=0)
    if lifes: 
        life = lifes[0]
        life.watch += 1
        life.save()
        return render(request,'school/show.html',{"life": life})
    else:
        return HttpResponseRedirect('/error')

def delete(request,id):
    if request.user.is_authenticated():
        if Life.objects.filter(user_id=request.user.id,id=id):
            life = Life.objects.get(user_id=request.user.id,id=id)
            life.delete()
            return HttpResponseRedirect('/user/'+str(request.user.id))
    else:
        return render(request, 'school/login.html')


def accept(request,id):
    if request.user.is_authenticated():
        lifes = Life.objects.filter(id=id)
        if lifes and (not lifes[0].accept):
            life = lifes[0]
            life.accept = 1
            life.accept_user = request.user.id
            life.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/error')
    else:
        return render(request, 'school/login.html')




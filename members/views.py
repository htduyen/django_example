from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render


def error404(request, exception):
    return render(request, '404.html', {})


# Create your views here.
def members(request):
    members = Member.objects.all().values()
    template = loader.get_template('login.html')
    context = {
        'mymembers': members
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'member': member
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


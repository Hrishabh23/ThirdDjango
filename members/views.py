from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def portfolio(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('testing.html')
    context = {
        'Name':"Hrishabh Nagar",
        'greeting':1,
        'day':"friday",
        #'greet':5,
        'fruits':['apple','Banana','cherry'],
    }
    return HttpResponse(template.render(context,request))

def testing2(request):
    mydata = Member.objects.all()
    mydata1 = Member.objects.all().values()
    mydata2 = Member.objects.values_list('phone')
    mydata3 = Member.objects.filter(firstname='Hrishabh').values()
    template = loader.get_template('testing2.html')
    context = {
        'mymembers':mydata,
        'mymembers1':mydata1,
        'mymembers2':mydata2,
        'mymembers3':mydata3,
    }
    return HttpResponse(template.render(context,request))
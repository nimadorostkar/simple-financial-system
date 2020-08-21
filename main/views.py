from django.shortcuts import render
from django.http import HttpResponse
from main.models import Finance


#def index(request):
#    finances = Finance.objects.all()
#    return render(request, 'index.html', {'finances':finances})


def index(request):
    template = "index.html"
    context = { 'Finance': Finance.objects.get(price=2000000) }
    return render(request, template, context)

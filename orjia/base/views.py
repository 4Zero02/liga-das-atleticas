from django.shortcuts import render

# Create your views here.


def home(request):
    template = 'base/base.html'
    return render(request, template)

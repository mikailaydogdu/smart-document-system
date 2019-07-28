from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.


def index(request):
    template_name = 'demo/index.html'
    return render(request, template_name)



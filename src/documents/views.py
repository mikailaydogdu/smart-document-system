from django.shortcuts import render

# Create your views here.
from documents.models import Documents


def index(request):
    template_name = "documents/index.html"
    qm = Documents.objects.all()
    context= { 'qm': qm }
    return render(request, template_name,context=context)
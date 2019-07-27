from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from demo.forms import DocumentForm
from demo.models import Code
from .serializers import FileSerializer


def index(request):
    template_name = 'demo/index.html'
    return render(request, template_name)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def exm(request):
    if request.method == 'post':
        form = DocumentForm(request.POST, user=request.user)
        if form.is_valid():
            uniquecode = form.cleaned_data.get('unique_code')
            user_defined_code = form.cleaned_data.get('user_defined_code')
            doc_code = Code(user_defined_code=user_defined_code, code=uniquecode)
            doc_code.save()
            doc = form.save(commit=False)
            doc.code = doc_code
            doc.save()
            return HttpResponse('success')
    else:
        form = DocumentForm(user=request.user)

    context = {'form': form, }

    return render_to_response('demo/exm.html', context, context_instance=RequestContext(request))

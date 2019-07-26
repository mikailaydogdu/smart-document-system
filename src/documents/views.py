from django.shortcuts import render
from django.contrib import messages

from SDS.myFuncitons import generate_sha
from documents.forms import DocumentForm, DocumentDetailForm
from documents.models import Documents, DocumentDetails


def home(request):
    template_name = "documents/home.html"
    qm = Documents.objects.all()
    context = {'qm': qm}
    return render(request, template_name, context=context)


# def filex(request):
#     form = DocumentForm(request.POST or None, request.FILES or None)
#
#     if form.is_valid():
#         form.save()
#         # form.save(commit=False)
#         # Documents.user = request.settings.AUTH_USER_MODEL = 'accounts.CustomUser'
#         messages.success(request, "Form kayıt işlemi başarılı")
#     return render(request, 'documents/image_form.html', {'form': form})


def filex(request):
    form = DocumentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        xfile = DocumentDetails(
            # document=request.POST['document'],
            file=request.FILES['file'],
            file_sha1=generate_sha(request.FILES['file'], )
        )


        user=request.user.id
        print(request.user.id)
        form.kk=user
        form.save(commit=True)
        xfile.save()
        # form.save(commit=False)
        # Documents.user = request.settings.AUTH_USER_MODEL = 'accounts.CustomUser'
        messages.success(request, "Form kayıt işlemi başarılı")
    return render(request, 'documents/image_form.html', {'form': form})


def file_detail(request):
    form = DocumentDetailForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        xfile = DocumentDetails(
            document=request.POST['document'],
            file=request.FILES['file'],
            file_sha1=generate_sha(request.FILES['file'], )
        )
        xfile.save()
        messages.success(request, 'Döküman ekleme başarılı.')
        return render(request, 'documents/home.html', {'form': form})
    form = DocumentDetailForm()
    context = {'form': form, }
    return render(request, 'documents/image_form.html', context)

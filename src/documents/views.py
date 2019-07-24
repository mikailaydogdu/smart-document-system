from django.shortcuts import render

# Create your views here.
from SDS.myFuncitons import generate_sha
from documents.froms import FileForm, imageForm
from documents.models import Documents, images


def home(request):
    template_name = "documents/home.html"
    qm = Documents.objects.all()
    context= { 'qm': qm }
    return render(request, template_name,context=context)


def fileuploads(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = Documents(
                payee=request.user,
                doc=request.FILES['Doc'],
                doc_sha1=generate_sha(request.FILES['Doc'],),
                title=form.cleaned_data.get('Title'),
                )
            file.save()
            return render(request, 'documents/image_form.html', {'form' : form})
    else:
        form = FileForm()
    context = {'form': form,}
    return render(request, 'documents/image_form.html', context)



def image(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            photo = images (
                # payee=request.user,
                image=request.FILES['Image'],
                image_sha1=generate_sha(request.FILES['Image'],),
                label=form.cleaned_data.get('Label'),
                )
            photo.save()
            return render(request, 'documents/image_form.html', {'form' : form})
    else:
        form = imageForm()
    context = {'form': form,}
    return render(request, 'documents/image_form.html', context)
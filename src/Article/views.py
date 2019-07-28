from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from Article.forms import ArticleAddForm, ArticleUpdateForm
from Article.models import Article, Revisions, Author
from SDS.myFuncitons import generate_sha


def home(request):
    template_name = "documents/home.html"
    qm = Article.objects.all()
    context = {'qm': qm}
    return render(request, template_name, context=context)


def article_add(request):
    form = ArticleAddForm(request.POST or None)
    if form.is_valid():
        xauth = Author(
            auth_name=request.POST['auth_name']
        )
        form.save(commit=True)
        xauth.save()
        messages.success(request, 'Döküman ekleme başarılı.')
        return render(request, 'documents/home.html', {'form': form})
    context = {'form': form, }
    return render(request, 'documents/image_form.html', context)


def article_update(request):
    form = ArticleUpdateForm(request.POST or None, request.FILES or None, request=request)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request, 'Döküman ekleme başarılı.')
        return render(request, 'documents/home.html', {'form': form})
    context = {'form': form, }
    return render(request, 'documents/image_form.html', context)

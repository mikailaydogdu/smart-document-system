from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from Article.forms import ArticleAddForm, ArticleUpdateForm
from Article.models import Article, Author


class ArticleListView(ListView):
    model = Article
    paginate_by = 100
    template_name = "article/article_list.html"


def article_add(request):
    form = ArticleAddForm(request.POST or None)
    if form.is_valid():
        xauth = Author(
            auth_name=request.POST['auth_name']
        )
        form.save(commit=True)
        xauth.save()
        messages.success(request, 'Döküman ekleme başarılı.')
        return render(request, 'article/home.html', {'form': form})
    context = {'form': form, }
    return render(request, 'article/image_form.html', context)


def article_update(request):
    form = ArticleUpdateForm(request.POST or None, request.FILES or None, request=request)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request, 'Döküman ekleme başarılı.')
        return render(request, 'article/home.html', {'form': form})
    context = {'form': form, }
    return render(request, 'article/image_form.html', context)


def revizyon_list(request, pk):
    context = {

    }
    qs = get_object_or_404(Article, id=pk)
    context['qs'] = qs
    qs_2 = qs.revision_article.all()
    context['qs_2'] = qs_2
    return render(request, 'article/revision_list.html', context)

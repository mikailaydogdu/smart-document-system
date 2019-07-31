from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from Article.forms import ArticleCreateForm, ArticleItemCreateForm
from Article.models import Article, Revisions


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    paginate_by = 100
    template_name = "article/article_list.html"


class ArticleCreate(LoginRequiredMixin, CreateView):
    template_name = "article/image_form.html"
    form_class = ArticleCreateForm
    success_url = reverse_lazy('anasayfa')


class ArticleItemListView(LoginRequiredMixin, ListView):
    model = Revisions
    template_name = 'article/revision_list.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({
            # 'Article_list': Article.objects.all(),
            'Revision_list': Revisions.objects.all().filter(article_id=self.kwargs['pk']),
            # 'Author_list':  Revisions.objects.all().filter(article__authors=self.kwargs['pk']),
        })
        return kwargs


class ArticileItemCreate(LoginRequiredMixin, CreateView):
    template_name = "article/image_form.html"
    form_class = ArticleItemCreateForm
    success_url = reverse_lazy('anasayfa')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        # print(kwargs)
        return kwargs


# @login_required
# def revizyon_list(request, pk):
#     context = {
#
#     }
#     qs = get_object_or_404(Article, id=pk)
#     context['qs'] = qs
#     qs_2 = qs.revision_article.all()
#     context['qs_2'] = qs_2
#     print(context)
#     return render(request, 'article/revision_list.html', context)

# @login_required
# def article_add(request):
#     form = ArticleAddForm(request.POST or None)
#     if form.is_valid():
#         xauth = Author(
#             auth_name=request.POST['auth_name']
#         )
#         form.save(commit=True)
#         xauth.save()
#         messages.success(request, 'Döküman ekleme başarılı.')
#         return render(request, 'article/home.html', {'form': form})
#     context = {'form': form, }
#     return render(request, 'article/image_form.html', context)


#
# @login_required
# def article_update(request):
#     form = ArticleUpdateForm(request.POST or None, request.FILES or None, request=request)
#     if form.is_valid():
#         form.save(commit=True)
#         messages.success(request, 'Döküman ekleme başarılı.')
#         return render(request, 'article/home.html', {'form': form})
#     context = {'form': form, }
#     return render(request, 'article/image_form.html', context)
#

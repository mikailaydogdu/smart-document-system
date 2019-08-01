from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from Article.forms import ArticleCreateForm, ArticleItemCreateForm
from Article.models import Article, Revisions


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    paginate_by = 100
    template_name = "article/article_list.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/image_form.html"
    form_class = ArticleCreateForm
    success_url = reverse_lazy('anasayfa')


class ArticleItemListView(LoginRequiredMixin, ListView):
    model = Revisions
    template_name = 'article/revision_list.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data()
        kwargs.update({
            # 'Article_list': Article.objects.all(),
            'Revision_list': Revisions.objects.filter(article_id=self.kwargs['pk']),
            # 'Author_list':  Revisions.objects.all().filter(article__authors=self.kwargs['pk']),
        })
        print(kwargs)
        return kwargs



class ArticileItemCreate(LoginRequiredMixin, CreateView):
    # model = Revisions
    template_name = "article/image_form.html"
    form_class = ArticleItemCreateForm
    success_url = reverse_lazy('anasayfa')


    def get_form_kwargs(self):
        context = super(ArticileItemCreate,self).get_form_kwargs()
        context['request'] = self.request
        context['article_id'] = self.kwargs["pk"]
        print(context)
        return context
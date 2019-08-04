from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from Article.forms import ArticleCreateForm, ArticleItemCreateForm
from Article.models import Article, Revisions
from Article.serializers import ArticleSerializer, RrevisionSerializer

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    paginate_by = 100
    template_name = "article/article_list.html"

    def get_queryset(self):
        queryset=self.model.objects.filter(active=True)
        return queryset



class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/image_form.html"
    form_class = ArticleCreateForm
    success_url = reverse_lazy('anasayfa')



class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer


    def get_object(self, queryset= None):
        return super(ArticleViewSet, self).get_object()

    def get_queryset(self):
        return Article.objects.filter(active=True)

    def performe_create(self, serializer):
        serializer.save()


class ArticleItemListView(LoginRequiredMixin, ListView):
    model = Revisions
    template_name = 'article/revision_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleItemListView, self).get_context_data(**kwargs)
        context.update({
            'Revision_list': Revisions.objects.filter(article_id=self.kwargs['pk']),})
        context['article_id']=self.kwargs['pk']
        return context



class ArticileItemCreate(LoginRequiredMixin, CreateView):
    template_name = "article/image_form.html"
    form_class = ArticleItemCreateForm
    success_url = reverse_lazy('anasayfa')

    def get_form_kwargs(self):
        context = super(ArticileItemCreate, self).get_form_kwargs()
        context['request'] = self.request
        context['article_id'] = self.kwargs["pk"]
        # print(context)
        return context

class ArticleItemViewSet(ModelViewSet):
    serializer_class = RrevisionSerializer


    def get_object(self, queryset= None):
        return super(ArticleItemViewSet, self).get_object()

    def get_queryset(self):
        return Revisions.objects.all()

    def performe_create(self, serializer):
        serializer.save()


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Revisions
    template_name = "article/detail.html"



class ArticleSearchView(ListView):
    model = Revisions
    template_name = 'article/searchresults.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_result = Revisions.objects.filter(
            Q(article__title__icontains=query)
            | Q(article__authors__auth_name__icontains=query)
            | Q(comment__icontains=query)

        )
        return search_result

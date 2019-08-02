from django_tables2 import tables, TemplateColumn
from Article.models import *


class ArticleTable(tables.Table):
    class Meta:
        model = Revisions
        attrs = {'class', 'table table-sm'}
        fields = '__all__'

    # edit = TemplateColumn(template_name='article/rlist.html')
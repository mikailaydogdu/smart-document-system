from django import forms

from Article.models import Revisions, Article
from SDS.myFuncitons import generate_md5


class ArticleCreateForm(forms.ModelForm):
    auth_name = forms.CharField(max_length=32)

    class Meta:
        model = Article
        fields = ['title', 'type', 'active', 'auth_name']
        # fields = '__all__'


class ArticleItemCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.article_id = kwargs.pop('article_id')
        super(ArticleItemCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        file = self.cleaned_data.get('file')
        md5 = generate_md5(file)
        if Revisions.objects.filter(file_sha1=md5).exists():
            raise forms.ValidationError('Eklemeye Çalıştığınız dosya istemde mevcut')
        # TODO: sistemde bulunan dosya bilgisi verilecek
        if not file:
            raise forms.ValidationError('Lütfen dosya ekini ekleyiniz.')

    def save(self, commit=True):
        model = self.Meta.model
        create = model.objects.create(
            article_id=self.article_id,
            file=self.cleaned_data["file"],
            comment=self.cleaned_data["comment"],
            uploader=self.request.user,
            file_sha1=generate_md5(file=self.cleaned_data["file"].open())
        )
        return create

    class Meta:
        model = Revisions
        fields = ['file','comment']
        labels = dict(file=('Dosya'), comment=('Açıklama'))

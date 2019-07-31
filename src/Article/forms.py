from django import forms

from Article.models import Revisions, Article
from SDS.myFuncitons import generate_md5


class ArticleCreateForm(forms.ModelForm):
    auth_name = forms.CharField(max_length=32)

    class Meta:
        model = Article
        fields = ['title', 'active', 'auth_name']


class ArticleItemCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

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
        return model.objects.create(
            article=self.cleaned_data["article"],
            file=self.cleaned_data["file"],
            comment=self.cleaned_data["comment"],
            uploader=self.request.user,
            file_sha1=generate_md5(file=self.request.FILES['file'], )
        )


    class Meta:
        model = Revisions
        fields = ['article', 'file', 'comment']
        labels = {
            'article': ('Dosya Tanımı'),
            'file': ('Dosya'),
            'comment': ('Açıklama'),
        }

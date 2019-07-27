from django import forms
from django.forms import ModelForm

from SDS.myFuncitons import generate_sha
from documents.models import Documents, DocumentDetails


# class DocumentForm(ModelForm):
#     class Meta:
#         model = Documents
#         fields = '__all__'


class DocumentForm(ModelForm):
    file = forms.FileField(required=True)
    class Meta:
        model = Documents
        # fields = '__all__'
        fields = ['file','label','type','comment','follow','active']

    def clean(self):

        #cleaned_data = super(DocumentForm, self).clean()
        file = self.cleaned_data.get('file')
        sha1 = generate_sha(file)

        if DocumentDetails.objects.filter(file_sha1=sha1).exists():
            raise forms.ValidationError('Eklemeye çalıştığınız dosya sistemede mevcut')
        if not file:
            raise forms.ValidationError('Dosya eklemeyi unuttunuz')



class DocumentDetailForm(ModelForm):
    file = forms.FileField(required=True)
    class Meta:
        model = DocumentDetails
        fields = ['document','file']

    def clean(self):
        cleaned_data = super(DocumentDetailForm, self).clean()
        file = cleaned_data.get('file')
        sha1 = generate_sha(file)
        if DocumentDetails.objects.filter(file_sha1=sha1).exists():
            raise forms.ValidationError('Eklemeye çalıştığınız dosya sistemede mevcut')
        if not file:
            raise forms.ValidationError('Dosya eklemeyi unuttunuz')




######################3from


class DemoForm(ModelForm):
    file = forms.FileField(required=True)
    class Meta:
        model = Documents
        # fields = '__all__'
        fields = ['file','label','type','comment','follow','active']

    def clean(self):

        cleaned_data = super(DemoForm, self).clean()
        file = self.cleaned_data.get('file')
        sha1 = generate_sha(file)

        if DocumentDetails.objects.filter(file_sha1=sha1).exists():
            raise forms.ValidationError('Eklemeye çalıştığınız dosya sistemede mevcut')
        if not file:
            raise forms.ValidationError('Dosya eklemeyi unuttunuz')
from django import forms

from SDS.myFuncitons import generate_sha
from documents.models import Documents, images


class FileForm(forms.Form):
    Title = forms.CharField(max_length=21, required=True)
    Doc = forms.FileField(required=True)

    def clean(self):
        cleaned_data = super(FileForm, self).clean()
        Title = cleaned_data.get('Title')
        Doc = cleaned_data.get('Doc')
        sha1 = generate_sha(Doc)
        if Documents.objects.filter(doc_sha1=sha1).exists():
            raise forms.ValidationError('This already exists')
        if not Title:
            raise forms.ValidationError('No Label')
        if not Doc:
            raise forms.ValidationError('No Image')


class imageForm(forms.Form):
    Label = forms.CharField(max_length=21, required=True)
    Image = forms.ImageField(required=True)

    def clean(self):
        cleaned_data = super(imageForm, self).clean()
        Label = cleaned_data.get('Label')
        Image = cleaned_data.get('Image')
        sha1 = generate_sha(Image)
        if images.objects.filter(image_sha1=sha1).exists():
            raise forms.ValidationError('This already exists')
        if not Label:
            raise forms.ValidationError('No Label')
        if not Image:
            raise forms.ValidationError('No Image')
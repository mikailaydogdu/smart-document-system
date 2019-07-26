from django.forms import ModelForm, forms

from demo.models import Document, UserDefinedCode


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ('code',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['user_defined_code']=forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=user))
        self.fields['unique_code']=forms.CharField(max_length=15)
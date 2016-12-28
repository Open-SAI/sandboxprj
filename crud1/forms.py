from django.forms import ModelForm, Textarea, TextInput, URLInput
from .models import Hackening
 
class HackeningForm(ModelForm):
    class Meta:
        model = Hackening
        fields = ['title', 'url', 'content']
        widgets = {
            'content': Textarea(attrs={'class':'form-control', 'rows': 4}),
            'url': URLInput(attrs={'class':'form-control'}),
            'title': TextInput(attrs={'class':'form-control'}),
        }

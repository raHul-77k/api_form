from django.forms import ModelForm
from .models import category

class entryForm(ModelForm):
    class Meta:
        model = category 
        fields = '__all__'


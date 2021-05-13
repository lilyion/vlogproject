from django import forms
from .models import Vlog

class CreatePostForm(forms.ModelForm):
    class Meta: 
      model = Vlog
      fields = ['titlee','comment']
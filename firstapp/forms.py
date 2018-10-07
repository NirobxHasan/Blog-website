from django import forms
from firstapp.models import Blog

class NewBlog(forms.ModelForm):
    class Meta():
        model = Blog
        fields = '__all__'

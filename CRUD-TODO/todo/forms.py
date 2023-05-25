from django import forms
from .models import Todo

# 폼을 활용하여 템플릿 작성
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')
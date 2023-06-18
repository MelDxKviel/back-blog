from django import forms

from .models import Post, Category


class PostCreateForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 15, 'cols': 45}))
    category = forms.ModelChoiceField(queryset=Category.objects.get_queryset())


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

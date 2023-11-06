from django import forms

from .models import Category, Tag, Post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 15, 'cols': 45, "class": "form-control"}))
    image = forms.ImageField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.get_queryset(),
                                      widget=forms.Select(attrs={"class": "form-control"}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.get_queryset(),
                                          widget=forms.SelectMultiple(attrs={"class": "form-control"}),
                                          required=False)

    class Meta:
        model = Post
        fields = ["title", "content", "image", "category", "tags",]


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, "class": "form-control"}))


class CategoryCreateForm(forms.Form):
    category_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))


class TagCreateForm(forms.Form):
    tag_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

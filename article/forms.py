from django import forms
from .models import Article
from django.contrib.admin.widgets import AdminDateWidget


class ArticleForm(forms.ModelForm):
    publish = forms.DateField(widget=AdminDateWidget())
    expiration = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",


        ]



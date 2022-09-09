from dataclasses import field
from django import forms

from snippets.models import Comment, Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ("title", "code", "description")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fieldsはtupleで！
        # fields = ("text") だとstr型で、errorになる
        fields = ("text", )

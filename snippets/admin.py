from django.contrib import admin

from snippets.models import Snippet, Comment, Tag, Card


# Register your models here.
admin.site.register(Snippet)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Card)

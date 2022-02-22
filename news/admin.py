from django.contrib import admin
from .models import tags,Editor, Article

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)


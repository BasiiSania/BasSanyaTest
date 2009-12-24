from django.contrib import admin
from mysite.books.models import AuthRequest, Author


admin.site.register(AuthRequest)
admin.site.register(Author)
from django.contrib import admin
from mysite.mydata.models import AuthRequest, Author, LogDB


admin.site.register(AuthRequest)
admin.site.register(Author)
admin.site.register(LogDB)
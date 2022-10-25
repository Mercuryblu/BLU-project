from django.contrib import admin
from .models import Diary


"""
admin 커스터마이징, Model Admin 
 - https://wayhome25.github.io/django/2017/03/22/django-ep8-django-admin/
"""

class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'create_at'] # 필드 목록
    list_display_links = [ 'user', 'title' ] # 링크 지정

admin.site.register(Diary, PostAdmin)
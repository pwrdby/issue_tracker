from django.contrib import admin

from tracker.models import Category, Issue
# Register your models here.
admin.site.register(Category)
admin.site.register(Issue)
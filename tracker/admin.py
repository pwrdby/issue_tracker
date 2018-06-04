from django.contrib import admin

from tracker.models import Category, Issue
from tracker.forms import CategoryAdminForm

class IssueAdmin(admin.ModelAdmin):
    """
    Own form with different 'description' field.
    """
    form = CategoryAdminForm
# Register your models here.
admin.site.register(Category)
admin.site.register(Issue, IssueAdmin)
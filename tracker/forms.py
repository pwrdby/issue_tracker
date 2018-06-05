from django import forms
from django.forms import widgets

from tracker.models import Category

class CategoryForm(forms.Form):
    """
    Form for changing categories on issue_list page.
    """

    def __init__(self, *args, **kwargs):
        """
        Init for this form. Create choices from issue categories.
        """
        super().__init__(*args, **kwargs)
        choices = [(cat.name, cat.name) for cat in Category.objects.all()]
        choices = [('all', '---')] + choices
        self.fields['current_category'] = forms.ChoiceField(choices=choices, required=False, 
                                                            label="Showing category is:")


class CategoryAdminForm(forms.ModelForm):
    """
    Change field for descrption in administration.
    """
    class Meta:
            model = Category
            widgets = {
                'description': widgets.Textarea(),
            }
            fields = '__all__'


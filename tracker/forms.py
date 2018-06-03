from django import forms
from django.forms import widgets

from tracker.models import Category

class CategoryForm(forms.Form):

    # current_category = forms.ChoiceField(choices=[('adada', 'aaa')])

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(*args, **kwargs)
        # print(dir(self.fields['current_category']))
        choices = [(cat.name, cat.name) for cat in Category.objects.all()]
        # choices = (('aa', ''))
        self.fields['current_category'] = forms.ChoiceField(choices=choices,required=False)


class CategoryAdminForm(forms.ModelForm):
    class Meta:
            model = Category
            widgets = {
                'description': widgets.Textarea(),
            }
            fields = '__all__'


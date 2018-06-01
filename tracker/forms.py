from django import forms

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

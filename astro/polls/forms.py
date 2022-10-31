from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from polls.models import Question, Choice


class PollsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super(PollsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))

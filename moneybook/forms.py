from django import forms

from .models import Spending


class DateInput(forms.DateInput):
    input_type = 'date'


# 記録
# 支出
class SpendingCreateForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

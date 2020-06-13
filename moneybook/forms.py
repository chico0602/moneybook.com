from django import forms

from .models import Spending


# 記録
# 支出
class SpendingCreateForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = '__all__'

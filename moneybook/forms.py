import bootstrap_datepicker_plus as datetimepicker
from django import forms
from django.utils import timezone

from .models import Spending, Income

#記録
class SpendingCreateForm(forms.ModelForm):
    S_CATEGORY = (
        (1, '食費'),
        (2, '日用雑貨'),
        (3, '娯楽'),
        (4, '交通費'),
        (5, '光熱費'),
        (6, 'その他'),
    )
    s_category = forms.ChoiceField(label='カテゴリー',choices=S_CATEGORY,required=True,)

    class Meta:
        model = Spending
        fields = '__all__'
        labels = {
            'description' : '品名',
            's_category' : 'カテゴリ',
            'money' : '金額',
            'useday' : '使用日',
            'note' : 'メモ',
        }
        widget = {
            'description' : forms.TextInput(attrs={'class': 'form-control'}),
            's_category' : forms.Select(attrs={'class': 'form-control'}),
            'money' : forms.TextInput(attrs={'class': 'form-control'}),
            'useday' : forms.DateInput(attrs={'class': 'form-control'}),
            'note' : forms.TextInput(attrs={'class': 'form-control'}),
        }


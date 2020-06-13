from django.contrib import admin
from .models import S_Category, Spending
# Register your models here.


# 支出テーブルのカラム
class SpendingAdmin(admin.ModelAdmin):
    list_display = ('description', 's_category', 'money', 'date', 'note')


admin.site.register(S_Category)
admin.site.register(Spending, SpendingAdmin)

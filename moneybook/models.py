from django.db import models
from django.utils import timezone

# Create your models here.


# 記録画面
# 支出カテゴリー
class S_Category(models.Model):
    class Meta:
        db_table = "s_category"
        verbose_name = "支出カテゴリ"
        verbose_name_plural = "支出カテゴリ"

    s_category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.s_category_name


# 支出
class Spending(models.Model):
    class Meta:
        db_table = "spending"
        verbose_name = "支出"
        verbose_name_plural = "支出"

    description = models.CharField('品名', max_length=50, null=True, blank=True)
    s_category = models.ForeignKey(S_Category, on_delete=models.PROTECT, verbose_name="支出カテゴリ")
    money = models.IntegerField('金額', default=0)
    date = models.DateField('使用日', default=timezone.now)
    note = models.TextField('メモ', blank=True)

    def __str__(self):
        return '品名:{} カテゴリ:{} メモ：{}'.format(self.description, self.s_category, self.note)

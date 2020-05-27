from django.db import models
from django.utils import timezone

# Create your models here.


#記録画面
#支出
class Spending(models.Model):
    S_CATEGORY = (
        (1, '食費'),
        (2, '日用雑貨'),
        (3, '娯楽'),
        (4, '交通費'),
        (5, '光熱費'),
        (6, 'その他'),
    )

    description = models.CharField('品名',max_length=50, null=True, blank=True)
    s_category = models.IntegerField('カテゴリー', choices=S_CATEGORY, null=True, blank=True)
    money = models.IntegerField('金額',default=0)
    
    useday = models.DateField('使用日', default=timezone.now)
    note = models.TextField('メモ', blank=True)

    def __str__(self):
        return '品名:{} カテゴリ:{} メモ：{}'.format(self.description,self.s_category, self.note)


#収入
class Income(models.Model):
    I_CATEGORY = (
        (1, '給与所得'),
        (2, '賞与'),
        (3, '臨時収入'),
        (4, 'その他'),
    )

    i_category = models.IntegerField('カテゴリー', choices=I_CATEGORY, null=True, blank=True)
    money = models.IntegerField('金額',default=0)
    
    inday = models.DateField('入金日', default=timezone.now)
    note = models.TextField('メモ', blank=True)

    def __str__(self):
        
        return 'カテゴリ:{} メモ:{}'.format(self.i_category, self.note)
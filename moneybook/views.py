from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db import models
from django.db.models import Sum
from django.contrib import messages
from .models import S_Category, Spending
from .forms import SpendingCreateForm
import calendar


# Create your views here

# ログイン
def index(request):
    return render(request, 'moneybook/index.html')


# 記録
class InputCreate(generic.CreateView):

    form_class = SpendingCreateForm
    template_name = "moneybook/input.html"
    success_url = reverse_lazy('moneybook:input')

    def form_valid(self, form):
        messages.success(self.request, '登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '登録に失敗しました。')
        return super().form_invalid(form)


# 更新削除
# 支出
class SpendingDetail(generic.DetailView):
    model = Spending
    template_name = "moneybook/s_detail.html"


class SpendingUpdate(generic.UpdateView):
    model = Spending
    form_class = SpendingCreateForm
    template_name = "moneybook/input.html"
    success_url = reverse_lazy('moneybook:history')

    def form_valid(self, form):
        messages.success(self.request, '更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '更新できませんでした。')
        return super().form_invalid(form)


class SpendingDelete(generic.DeleteView):
    model = Spending
    success_url = reverse_lazy('moneybook:history')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.error(self.request, '削除しました。')
        return result


# 履歴
class InputList(generic.ListView):
    model = Spending
    ordering = '-date'
    template_name = "moneybook/history.html"


# 分析
def show_circle_grahp(request):

    spending_data = Spending.objects.all()

    total = 0
    for item in spending_data:
        total += item.money

    s_category_list = []

    s_category_data = S_Category.objects.all()

    for item in s_category_data:
        s_category_list.append(item.s_category_name)

    s_category_ratio = {}
    s_category_num = []
    for i, item in enumerate(s_category_list):
        s_category_total = Spending.objects.filter(s_category__s_category_name=s_category_list[i]).aggregate(sum=models.Sum('money'))['sum']

        if s_category_total != None:
            ratio = int((s_category_total / total) * 100)
            s_category_num.append(s_category_total)
            s_category_ratio[item] = ratio
        else:
            ratio = 0
            s_category_num.append(0)
            s_category_ratio[item] = ratio

    return render(request, 'moneybook/analysis.html', {
        's_category_ratio': s_category_ratio,
        'total': total,
        's_category_num': s_category_num,
    })


# 総分析
def show_total_grahp(request):
    spending_data = Spending.objects.all()

    # カテゴリリストのデータ
    category_list = []
    category_data = S_Category.objects.all().order_by('-s_category_name')
    for item in category_data:
        category_list.append(item.s_category_name)

    # 日付データ
    date_list = []
    for i in spending_data:
        date_list.append((i.date.strftime('%Y/%m/%d')[:7]))
        date_list.sort()

        x_label = list(set(date_list))
        x_label.sort(reverse=False)

    # 月毎＆カテゴリ毎の合計金額データ
    monthly_sum_data = []
    for i in range(len(x_label)):
        year, month = x_label[i].split("/")
        month_range = calendar.monthrange(int(year), int(month))[1]
        first_date = year + '-' + month + '-' + '01'
        last_date = year + '-' + month + '-' + str(month_range)
        # 1か月分のデータ取得
        total_of_month = Spending.objects.filter(date__range=(first_date, last_date))
        category_total = total_of_month.values('s_category').annotate(total_price=Sum('money'))

        for j in range(len(category_total)):
            money = category_total[j]['total_price']
            s_category = S_Category.objects.get(pk=category_total[j]['s_category'])
            monthly_sum_data.append([x_label[i], s_category.s_category_name, money])

    # 折れ線グラフカラー
    border_color_list = ['254,97,132,0.8','54,164,235,0.8','0,255,65,0.8','255,241,15,0.8',\
                        '255,94,25,0.8','84,77,203,0.8','204,153,50,0.8','214,216,165,0.8',\
                        '33,30,45,0.8','52,38,89,0.8']
    border_color = []
    for x, y in zip(category_list, border_color_list):
        border_color.append([x, y])

    background_color_list = ['254,97,132,0.5','54,164,235,0.5','0,255,65,0.5','255,241,15,0.5',\
                            '255,94,25,0.5','84,77,203,0.5','204,153,50,0.5','214,216,165,0.5'\
                            '33,30,45,0.5','52,38,89,0.5']
    background_color = []
    for x, y in zip(category_list, background_color_list):
        background_color.append([x, y])

    # 数字のないカテゴリーに0を入れる
    matrix_list = []
    for item_label in x_label:
        for item_category in category_list:
            matrix_list.append([item_label, item_category, 0])

    for yyyy_mm, s_category, total in monthly_sum_data:
        for i, data in enumerate(matrix_list):
            if data[0] == yyyy_mm and data[1] == s_category:
                matrix_list[i][2] = total

    return render(request, 'moneybook/total_analysis.html', {
        'x_label' : x_label,
        'category_list' : category_list,
        'border_color' : border_color,
        'background_color': background_color,
        'matrix_list' : matrix_list,
    })

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Spending, Income
from .forms import SpendingCreateForm



# Create your views here

#ログイン
def index(request):
    return render(request, 'moneybook/index.html')


#記録
class SpendingCreate(generic.CreateView):
    model = Spending
    form_class = SpendingCreateForm
    template_name = "moneybook/input.html"
    success_url = reverse_lazy('moneybook:input')

    def form_valid(self, form):
        messages.success(self.request, '登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '登録に失敗しました。')
        return super().form_invalid(form)    
    
#更新削除
#支出
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
        messages.error(self.request, '削除しました。') # 追加
        return result

#履歴
class SpendingList(generic.ListView):
    model = Spending
    ordering = '-useday'
    template_name = "moneybook/history.html"



#分析
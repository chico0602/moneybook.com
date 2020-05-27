from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
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
    
    
    
#履歴
class SpendingList(generic.ListView):
    model = Spending
    ordering = '-useday'
    template_name = "moneybook/history.html"
    
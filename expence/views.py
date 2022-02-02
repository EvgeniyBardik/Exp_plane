from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import IncomeForm, SpendingForm, SavingForm
from django.urls import reverse_lazy

from .models import Income, Spending, Saving

from .func import sum

def index(request):
	inco = Income.objects.all()
	spen = Spending.objects.all()
	savi = Saving.objects.all()
	sum_inco = sum(Income)
	sum_spen = sum(Spending)
	sum_savi = sum(Saving) 
	context = {'inco': inco, 'sum_inco': sum_inco, 'sum_spen': sum_spen, 'sum_savi': sum_savi, 'spen': spen, 'savi': savi}
	return render(request, 'expence/index.html', context)
	
def inc(request):
	inco = Income.objects.all()
	sum_inco = sum(Income)
	context = {'inco': inco, 'sum_inco': sum_inco}
	return render(request, 'expence/income.html', context)

def spe(request):
	spen = Spending.objects.all()
	sum_spen = sum(Spending)
	context = {'spen': spen, 'sum_spen': sum_spen}
	return render(request, 'expence/spending.html', context)

def sav(request):
	savi = Saving.objects.all()
	sum_savi = sum(Saving)
	context = {'savi': savi, 'sum_savi': sum_savi}
	return render(request, 'expence/saving.html', context)

class AddCreateView(CreateView):
	template_name = 'expence/create.html'
	
	
class IncomeCreateView(AddCreateView):
	form_class = IncomeForm
	success_url = reverse_lazy('inc')
	
class SpendingCreateView(AddCreateView):
	form_class = SpendingForm
	success_url = reverse_lazy('spe')
	
class SavingCreateView(AddCreateView):
	form_class = SavingForm
	success_url = reverse_lazy('sav')

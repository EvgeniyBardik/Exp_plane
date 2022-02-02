from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import IncomeForm, SpendingForm, SavingForm
from django.urls import reverse_lazy
from django.db.models import Sum
from .models import Income, Spending, Saving

sum_inco = Income.objects.aggregate(val=Sum('amount'))['val']
sum_spen = Spending.objects.aggregate(val=Sum('amount'))['val']
sum_savi = Saving.objects.aggregate(val=Sum('amount'))['val']

def index(request):
	inco = Income.objects.all()
	spen = Spending.objects.all()
	savi = Saving.objects.all()
	context = {'inco': inco, 'sum_inco': sum_inco, 'sum_spen': sum_spen, 'sum_savi': sum_savi, 'spen': spen, 'savi': savi}
	return render(request, 'expence/index.html', context)
	
def inc(request):
	inco = Income.objects.all()
	context = {'inco': inco, 'sum_inco': sum_inco}
	return render(request, 'expence/income.html', context)

def spe(request):
	spen = Spending.objects.all()
	context = {'spen': spen, 'sum_spen': sum_spen}
	return render(request, 'expence/spending.html', context)

def sav(request):
	savi = Saving.objects.all()
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

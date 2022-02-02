from django.forms import ModelForm

from .models import Income, Spending, Saving

class IncomeForm(ModelForm):
	class Meta:
		model = Income
		fields = ('title', 'amount')
		
class SpendingForm(ModelForm):
	class Meta:
		model = Spending
		fields = ('title', 'amount')
		
class SavingForm(ModelForm):
	class Meta:
		model = Saving
		fields = ('title', 'amount')

from django.urls import path

from .views import index, IncomeCreateView, SpendingCreateView, SavingCreateView, inc, sav, spe

urlpatterns = [
	path('addinc/', IncomeCreateView.as_view(), name='addinc'),
	path('addspe/', SpendingCreateView.as_view(), name='addspe'),
	path('addsav/', SavingCreateView.as_view(), name='addsav'),
	path('inc/', inc, name='inc'),
	path('spe/', spe, name='spe'),
	path('sav/', sav, name='sav'),
	path('', index, name='index'),
]

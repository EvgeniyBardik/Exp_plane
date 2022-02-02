from django.db import models

class Transaction(models.Model):
	title = models.CharField(max_length=50, verbose_name='Имя')
	amount = models.FloatField(null=True, blank=False, verbose_name='Сумма')
	date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name = 'Дата')
	def __str__(self):
		return self.title

class Income(Transaction):

	class Meta:
		verbose_name_plural = 'Доходы'
		verbose_name = 'Доход'
		ordering = ['date']

class Spending(Transaction):

	class Meta:
		verbose_name_plural = 'Расходы'
		verbose_name = 'Расход'
		ordering = ['date']

class Saving(Transaction):

	class Meta:
		verbose_name_plural = 'Сбережения'
		verbose_name = 'Сбережения'
		ordering = ['date']		
	

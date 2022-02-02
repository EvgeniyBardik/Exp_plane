from django.contrib import admin

from .models import Income, Spending, Saving

class ExAdmin(admin.ModelAdmin):
	list_display = ('title', 'amount', 'date')
	list_display_links = ('title', 'amount')
	search_fields = ('title', )
	
admin.site.register(Income, ExAdmin)
admin.site.register(Spending, ExAdmin)
admin.site.register(Saving, ExAdmin)

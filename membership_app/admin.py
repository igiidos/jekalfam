from django.contrib import admin
from .models import YearList, MonthList, FeeManager


admin.site.register(YearList)


class MonthListAdmin(admin.ModelAdmin):
	list_display = ('pk', 'make_year', 'choice_month')


admin.site.register(MonthList, MonthListAdmin)


class FeeManagerAdmin(admin.ModelAdmin):
	list_display = ('select_month', 'members', 'money', 'status')


admin.site.register(FeeManager, FeeManagerAdmin)

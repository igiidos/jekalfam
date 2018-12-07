from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import FeeManager, MonthList, YearList

# Create your views here.


@ login_required
def monthly_list(request):
	month_list = MonthList.objects.all()
	month_count = month_list.count()
	total_fee = FeeManager.objects.filter(using='in')
	total_in = total_fee.aggregate(Sum('money'))
	total_out = FeeManager.objects.filter(using='out').aggregate(Sum('money'))
	total_less = (month_count * 12 - total_fee.count())*10000
	total_result = total_in['money__sum'] - total_out['money__sum']

	# for month in month_list:
	# 	if month.feemanager_set.all():
	# 		monthly_in = month.feemanager_set.filter(using='in', status='on').aggregate(Sum('money'))
	# 		print(monthly_in)
		# for fee_list in month.feemanager_set.filter(using='in', status='on'):
		# 	print("{}의 {}월 회비는 {}입니다.".format(fee_list.members, fee_list.select_month, fee_list.money))

	context = {
		'month_list': month_list,
		'total_in': total_in,
		'total_out': total_out,
		'total_less': total_less,
		'total_result': total_result,

	}
	return render(request, 'membership_app/monthly_list.html', context)


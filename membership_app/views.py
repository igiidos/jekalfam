from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import FeeManager, MonthList, YearList
from .forms import MonthListForm
from django.views.generic.edit import FormView

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

	context = {
		'month_list': month_list,
		'total_in': total_in,
		'total_out': total_out,
		'total_less': total_less,
		'total_result': total_result,

	}
	return render(request, 'membership_app/monthly_list.html', context)


@login_required
def add_month(request):
	if request.method == 'POST':
		form = MonthListForm(request.POST)
		if form.is_valid():
			post = form.save()
			post.save()
			return redirect('monthly_list')
	else:
		form = MonthListForm()
	context = {
		'form': form
	}
	return render(request, 'membership_app/add_month.html', context)


@login_required
def month_detail(request, pk):
	month = MonthList.objects.get(pk=pk)
	details = FeeManager.objects.filter(select_month=month, status='on')
	context = {
		'month': month,
		'details': details
	}
	return render(request, 'membership_app/month_detail.html', context)


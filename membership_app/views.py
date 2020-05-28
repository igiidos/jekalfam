from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import FeeManager, MonthList, YearList
from .forms import MonthListForm, AddFeeForm
from django.forms.formsets import formset_factory
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import IntegrityError

# Create your views here.


@ login_required
def monthly_list(request):
    month_list = MonthList.objects.all()
    total_fee = FeeManager.objects.filter(using='in')
    total_in = total_fee.aggregate(Sum('money'))
    expect_total = 0
    for month in month_list:
        each_month = month.expect_total_monthly_fee()
        expect_total += each_month

    total_less = expect_total - total_in['money__sum']

    if FeeManager.objects.filter(using='out'):
        total_out = FeeManager.objects.filter(using='out').aggregate(Sum('money'))
        total_result = total_in['money__sum'] - total_out['money__sum']
    else:
        total_out = 0
        total_result = total_in['money__sum']


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
    user_lists = get_user_model()
    month = MonthList.objects.get(pk=pk)
    details = FeeManager.objects.filter(select_month=month, status='on')

    context = {
        'month': month,
        'details': details,
    }
    return render(request, 'membership_app/month_detail.html', context)


def add_fee_formset(request, pk):
    bring_formset = formset_factory(AddFeeForm, extra=5)
    month = MonthList.objects.get(pk=pk)
    if request.method == 'POST':
        formset = bring_formset(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    post = form.save(commit=False)
                    if post.members != '회원명':
                        post.select_month = month
                        try:
                            post.save()
                        except IntegrityError:
                            pass
            return redirect('month_detail', pk)
    else:
        formset = bring_formset()

    context = {
        'formset': formset,
        'month': month,
    }
    return render(request, 'membership_app/add_fee_formset.html', context)


def fee_delete(request, month_pk, detail_pk):
    instance = FeeManager.objects.get(pk=detail_pk)
    instance.delete()
    pk = month_pk
    return redirect('month_detail', pk)


def fee_update(request, month_pk, detail_pk):
    fee = FeeManager.objects.get(pk=detail_pk)
    month = MonthList.objects.get(pk=month_pk)
    if request.method == 'POST':
        forms = AddFeeForm(request.POST, instance=fee)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.select_month = month
            post.save()
            return redirect('month_detail', pk=month_pk)
    else:
        forms = AddFeeForm(instance=fee)

    context = {
        'month' : month,
        'forms': forms,
    }
    return render(request, 'membership_app/fee_update.html', context)
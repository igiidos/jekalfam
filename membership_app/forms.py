from django import forms
from .models import MonthList, FeeManager


class MonthListForm(forms.ModelForm):
	class Meta:
		model = MonthList
		fields = (
			'make_year',
			'choice_month',
		)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['make_year'].widget.attrs.update({'class': 'form-control'})
		self.fields['choice_month'].widget.attrs.update({'class': 'form-control'})


class AddFeeForm(forms.ModelForm):
	class Meta:
		model = FeeManager
		fields = (
			'members',
			'using',
			'money',
			'memo'
		)
		labels = {
			'members': '멤버',
			'using': '입/출금',
			'money': '금액',
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['members'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['using'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['money'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['memo'].widget.attrs.update({'class': 'form-control form-control-sm textarea-width', 'rows': '1'})

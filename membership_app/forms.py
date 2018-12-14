from django import forms
from .models import MonthList


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

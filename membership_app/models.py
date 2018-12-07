from django.db import models
from django.conf import settings
from django.db.models import Sum


choice_month = (
	('0', '월선택'),
	('1', '1월'),
	('2', '2월'),
	('3', '3월'),
	('4', '4월'),
	('5', '5월'),
	('6', '6월'),
	('7', '7월'),
	('8', '8월'),
	('9', '9월'),
	('10', '10월'),
	('11', '11월'),
	('12', '12월')
)

status_list = (
	('off', 'off'),
	('on', 'on')
)

using = (
	('in', '입금'),
	('out', '출금')
)


class YearList(models.Model):
	years = models.CharField(max_length=100)

	def __str__(self):
		return self.years


class MonthList(models.Model):
	make_year = models.ForeignKey('YearList', on_delete=models.CASCADE)
	choice_month = models.CharField(max_length=3, choices=choice_month, default='0')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def total_in(self):
		return self.feemanager_set.filter(status='on', using='in').aggregate(Sum('money'))

	def total_out(self):
		return self.feemanager_set.filter(status='on', using='out').aggregate(Sum('money'))

	def total_no_in(self):
		if self.total_in()['money__sum'] is None:
			return 120000
		if self.total_in() is not None:
			return 120000-int(self.total_in()['money__sum'])

	def __str__(self):
		return self.choice_month


class FeeManager(models.Model):
	select_month = models.ForeignKey('MonthList', on_delete=models.CASCADE)
	members = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	using = models.CharField(max_length=3, choices=using, default='in')
	money = models.IntegerField(default=10000)
	memo = models.TextField(blank=True)
	status = models.CharField(max_length=3, choices=status_list, default='on')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['select_month']

	def __str__(self):
		return str(self.select_month)


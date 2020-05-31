from django.db import models
from django.conf import settings
from django.db.models import Sum
from django.contrib.auth import get_user_model



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

members = (
    ('회원명', '회원명'),
    ('남영경', '남영경'),
    ('남영석', '남영석'),
    ('임용빈', '임용빈'),
    ('임영빈', '임영빈'),
    ('임규빈', '임규빈'),
    ('제갈익', '제갈익'),
    ('제갈륜', '제갈륜'),
    ('박수려', '박수려'),
    ('박민찬', '박민찬'),
    ('김은지', '김은지'),
    ('김병수', '김병수'),
    ('제갈민', '제갈민'),
    ('제갈웅', '제갈웅')
)

member_list = [
    '남영경', '남영석', '임용빈', '임영빈', '임규빈', '제갈익', '제갈륜', '박수려', '박민찬', '김은지', '김병수', '제갈민', '제갈웅'
]


class YearList(models.Model):
    years = models.CharField(max_length=100)

    def __str__(self):
        return self.years


class MonthList(models.Model):
    make_year = models.ForeignKey('YearList', on_delete=models.CASCADE)
    choice_month = models.CharField(max_length=3, choices=choice_month, default='0')
    month_fee = models.IntegerField(default=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def expect_total_monthly_fee(self):
        return self.month_fee * (len(members) - 1)

    def total_in(self):
        return self.feemanager_set.filter(status='on', using='in').aggregate(Sum('money'))

    def total_out(self):
        return self.feemanager_set.filter(status='on', using='out').aggregate(Sum('money'))

    def total_no_in(self):
        if self.total_in()['money__sum'] is None:
            return self.expect_total_monthly_fee()
        else:
            return self.expect_total_monthly_fee()-int(self.total_in()['money__sum'])

    def who_no_in(self):
        copy_all_members = member_list.copy()
        for paid in self.feemanager_set.filter(status='on', using='in'):
            name = paid.members
            if name in copy_all_members:
                copy_all_members.remove(name)

        return copy_all_members

    def __str__(self):
        return self.choice_month


class FeeManager(models.Model):
    select_month = models.ForeignKey('MonthList', on_delete=models.CASCADE)
    members = models.CharField(max_length=10, choices=members, default='회원명')
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


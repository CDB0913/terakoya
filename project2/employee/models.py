# https://www.youtube.com/watch?v=qQji8CbbwO8

from django.db import models
from django.utils import timezone

SALARY_CLASS_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
)

SALARY_RANK_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Department(models.Model):
    name = models.CharField("部門", max_length=20)
    created_at = models.DateTimeField("日付", default=timezone.now)

    def __str__(self):
        return self.name


class Segment(models.Model):
    name = models.CharField("セグメント", max_length=20)
    created_at = models.DateTimeField("日付", default=timezone.now)

    def __str__(self):
        return self.name


class CostType(models.Model):
    name = models.CharField("費用区分", max_length=20)
    created_at = models.DateTimeField("日付", default=timezone.now)

    def __str__(self):
        return self.name


class ContractType(models.Model):
    name = models.CharField("契約形態", max_length=20)
    created_at = models.DateTimeField("日付", default=timezone.now)

    def __str__(self):
        return self.name


class OtherAllowancesType(models.Model):
    name = models.CharField("その他手当", max_length=20)
    created_at = models.DateTimeField("日付", default=timezone.now)

    def __str__(self):
        return self.name


class Employee(models.Model):

    employee_id = models.CharField("社員番号", max_length=3, primary_key=True)
    employee_name = models.CharField("名前", max_length=20)
    email = models.EmailField("メールアドレス", blank=False)
    birth = models.DecimalField("生年月日(YYYYmmdd)", max_digits=8, decimal_places=0)
    date_of_entry = models.DecimalField("入社日(YYYYmmdd)", max_digits=8, decimal_places=0)
    department = models.ForeignKey(
        Department, verbose_name="部門", on_delete=models.PROTECT,
        )
    segment = models.ForeignKey(
        Segment, verbose_name="セグメント", on_delete=models.PROTECT,
    )
    cost_type = models.ForeignKey(
        CostType, verbose_name="費用区分", on_delete=models.PROTECT,
    )
    contract_type = models.ForeignKey(
        ContractType, verbose_name="契約形態", on_delete=models.PROTECT,
    )
    salary_class = models.PositiveSmallIntegerField("クラス", choices=SALARY_CLASS_CHOICES)
    salary_rank = models.PositiveSmallIntegerField("ランク", choices=SALARY_RANK_CHOICES)
    other_allowances_type = models.ForeignKey(
        OtherAllowancesType, verbose_name="その他手当", on_delete=models.PROTECT,
    )

    created_at = models.DateTimeField("日付", default=timezone.now)

    def __str__(self):
        return "{0} {1}".format(self.employee_id, self.employee_name)

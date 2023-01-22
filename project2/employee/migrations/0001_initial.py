# Generated by Django 4.1.3 on 2023-01-07 07:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='契約形態')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='CostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='費用区分')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='部門')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='OtherAllowancesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='その他手当')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='セグメント')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='社員番号')),
                ('employee_name', models.CharField(max_length=20, verbose_name='名前')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('birth', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='生年月日(YYYYmmdd)')),
                ('date_of_entry', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='入社日(YYYYmmdd)')),
                ('salary_class', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], verbose_name='クラス')),
                ('salary_rank', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='ランク')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
                ('contract_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.contracttype', verbose_name='契約形態')),
                ('cost_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.costtype', verbose_name='費用区分')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.department', verbose_name='部門')),
                ('other_allowances_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.otherallowancestype', verbose_name='その他手当')),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.segment', verbose_name='セグメント')),
            ],
        ),
    ]
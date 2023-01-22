from django.contrib import admin
from .models import Department, Segment, CostType, ContractType, OtherAllowancesType, Employee

admin.site.register(Department)
admin.site.register(Segment)
admin.site.register(CostType)
admin.site.register(ContractType)
admin.site.register(OtherAllowancesType)
admin.site.register(Employee)

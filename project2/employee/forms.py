from django import forms
from .models import Department, Segment, CostType, ContractType


class SearchForm(forms.Form):
    department = forms.ModelChoiceField(
        queryset=Department.objects,
        label="部門",
        required=False,
    )

    segment = forms.ModelChoiceField(
        queryset=Segment.objects,
        label="セグメント",
        required=False,
    )

    cost_type = forms.ModelChoiceField(
        queryset=CostType.objects,
        label="費用区分",
        required=False,
    )

    contract_type = forms.ModelChoiceField(
        queryset=ContractType.objects,
        label="契約形態",
        required=False,
    )

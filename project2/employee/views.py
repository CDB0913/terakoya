from django.views.generic import ListView
from .forms import SearchForm
from .models import Employee


class IndexView(ListView):
    model = Employee


def get_context_data(self):
    context = super().get_context_data()
    context["search_form"] = SearchForm(self.request.GET)
    return context


def get_queryset(self):
    form = SearchForm(self.request.GET)
    form.is_valid()

    queryset = super().get_queryset()

    department = form.cleaned_data["department"]
    if department:
        queryset = queryset.filter(department=department)

    segment = form.cleaned_data["segment"]
    if segment:
        queryset = queryset.filter(segment=segment)

    cost_type = form.cleaned_data["cost_type"]
    if cost_type:
        queryset = queryset.filter(cost_type=cost_type)

    contract_type = form.cleaned_data["contract_type"]
    if contract_type:
        queryset = queryset.filter(contract_type=contract_type)
    return queryset

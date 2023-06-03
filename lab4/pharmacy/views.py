from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import MedicineCategory


class IndexView(generic.TemplateView):
    template_name = "pharmacy/index.html"


class CategoriesIndexView(generic.ListView):
    template_name = "pharmacy/categories_index.html"
    context_object_name = "categories_list"

    def get_queryset(self):
        """
        Return the categories
        """
        return MedicineCategory.objects.order_by("-name")


class CategoriesDetailView(generic.DetailView):
    model = MedicineCategory
    template_name = "pharmacy/categories_detail.html"


class MedicinesIndexView(generic.ListView):
    pass


class MedicinesDetailView(generic.DetailView):
    pass


class SalesIndexView(generic.ListView):
    pass


class SalesDetailView(generic.DetailView):
    pass


class SalesAddView(generic.View):
    pass


class SuppliersIndexView(generic.ListView):
    pass


class SuppliersDetailView(generic.DetailView):
    pass

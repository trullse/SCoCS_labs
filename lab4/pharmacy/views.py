from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import MedicineCategory, Medicine, Supplier


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
    template_name = "pharmacy/medicines_index.html"
    context_object_name = "medicines_list"

    def get_queryset(self):
        """
        Return the medicines
        """
        return Medicine.objects.order_by("-name")


class MedicinesDetailView(generic.DetailView):
    model = Medicine
    template_name = "pharmacy/medicines_detail.html"


class SalesIndexView(generic.ListView):
    pass


class SalesDetailView(generic.DetailView):
    pass


class SalesAddView(generic.View):
    pass


class SuppliersIndexView(generic.ListView):
    template_name = "pharmacy/suppliers_index.html"
    context_object_name = "suppliers_list"

    def get_queryset(self):
        """
        Return the suppliers
        """
        return Supplier.objects.order_by("-name")


class SuppliersDetailView(generic.DetailView):
    model = Supplier
    template_name = "pharmacy/suppliers_detail.html"

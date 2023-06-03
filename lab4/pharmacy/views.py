from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "pharmacy/index.html"


class CategoriesIndexView(generic.ListView):
    pass


class CategoriesDetailView(generic.DetailView):
    pass


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

import logging
from datetime import datetime
import requests

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import MedicineCategory, Medicine, Supplier, Sale
from .helpers import plot_last_days_sales


logger = logging.getLogger('main')


class IndexView(generic.DetailView):
    logger.warning('in index view')
    template_name = "pharmacy/index.html"
    joke_info = {}
    model = joke_info

    def get(self, request, *args, **kwargs):
        logger.info('In index view')

        url = 'https://official-joke-api.appspot.com/jokes/programming/random'
        joke_info = requests.get(url).json()
        self.joke_info = joke_info
        logger.debug(joke_info)
        context = get_ip_request()
        logger.debug(f'context: {context}')

        return render(request, self.template_name, context)


def get_ip_request():
    logger.info('connecting to the joke API')
    url = 'https://official-joke-api.appspot.com/jokes/programming/random'
    ip_request = requests.get(url).json()
    ip_request = ip_request[0]
    setup = ip_request['setup']
    punchline = ip_request['punchline']
    logger.debug(ip_request)
    return {'setup': setup, 'punchline': punchline}


class CategoriesIndexView(generic.ListView):
    template_name = "pharmacy/categories_index.html"
    context_object_name = "categories_list"

    def get_queryset(self):
        """
        Return the categories
        """
        return MedicineCategory.objects.order_by("-name")

    def get(self, request, *args, **kwargs):
        logger.info('In categories index view')
        return super().get(request, *args, **kwargs)


class CategoriesDetailView(generic.DetailView):
    model = MedicineCategory
    template_name = "pharmacy/categories_detail.html"

    def get(self, request, *args, **kwargs):
        logger.info('In categories detail view')
        return super().get(request, *args, **kwargs)


class MedicinesIndexView(generic.ListView):
    template_name = "pharmacy/medicines_index.html"
    context_object_name = "medicines_list"

    def get_queryset(self):
        """
        Return the medicines
        """
        return Medicine.objects.order_by("-name")

    def get(self, request, *args, **kwargs):
        logger.info('In medicines index view')
        return super().get(request, *args, **kwargs)


class MedicinesDetailView(generic.DetailView):
    model = Medicine
    template_name = "pharmacy/medicines_detail.html"

    def get(self, request, *args, **kwargs):
        logger.info('In medicines detail view')
        return super().get(request, *args, **kwargs)


class SalesIndexView(PermissionRequiredMixin, generic.ListView):
    logger.info('In sales index view')
    permission_required = 'pharmacy.view_sale'
    template_name = "pharmacy/sales_index.html"
    context_object_name = "sales_list"

    def get_queryset(self):
        """
        Return the sales
        """
        return Sale.objects.order_by("-date")

    def get(self, request, *args, **kwargs):
        logger.info('In sales index view')
        return super().get(request, *args, **kwargs)


class SalesDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'pharmacy.view_sale'
    model = Sale
    template_name = "pharmacy/sales_detail.html"

    def get(self, request, *args, **kwargs):
        logger.info('In sales detail view')
        return super().get(request, *args, **kwargs)


class SuppliersIndexView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'pharmacy.view_supplier'
    template_name = "pharmacy/suppliers_index.html"
    context_object_name = "suppliers_list"

    def get_queryset(self):
        """
        Return the suppliers
        """
        return Supplier.objects.order_by("-name")

    def get(self, request, *args, **kwargs):
        logger.info('In suppliers index view')
        return super().get(request, *args, **kwargs)


class SuppliersDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'pharmacy.view_supplier'
    model = Supplier
    template_name = "pharmacy/suppliers_detail.html"

    def get(self, request, *args, **kwargs):
        logger.info('In suppliers detail view')
        return super().get(request, *args, **kwargs)


class SaleCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'pharmacy.add_sale'
    model = Sale
    fields = '__all__'
    initial = {'date': datetime.now(), }
    template_name = "pharmacy/sales_add.html"
    success_url = reverse_lazy('pharmacy:sale_index')

    def get(self, request, *args, **kwargs):
        logger.info('In sales add view')
        return super().get(request, *args, **kwargs)


class StatisticsView(PermissionRequiredMixin, generic.ListView):
    context_object_name = 'sales_list'
    permission_required = 'pharmacy.view_sale'
    template_name = 'pharmacy/statistics.html'

    def get(self, request, *args, **kwargs):
        logger.info('In statistics view')
        plot_last_days_sales()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """
        Return the sales
        """
        return Sale.objects.order_by("-date")

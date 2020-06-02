# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse

from . import models
from . import forms

# Create your views here.


def drug_list(request):
    drugs = models.Drug.objects.all()
    drug_types = {
        'drugs': drugs,
    }

    return render(request, 'inventory/inventory-main.html', drug_types)


class DrugAdd(FormView):
    template_name = 'inventory/add_new_drug.html'
    form_class = forms.DrugForm

    def form_valid(self, form):
        df = form.save()
        df.save()
        return redirect('drug-list')


class DrugUpdate(UpdateView):
    template_name = 'inventory/update_drug.html'  # Need to create
    model = models.Drug
    form_class = forms.DrugForm

    def form_valid(self, form):
        df = form.save()
        df.save()
        return redirect('drug-list')

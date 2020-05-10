# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from . import models
from . import forms

# Create your views here.


def drug_list(request):
    drugs = models.Drug.objects.all()
    drug_types = {
        'drugs': drugs,
    }

    return render(request, 'inventory/inventory-main.html', drug_types)

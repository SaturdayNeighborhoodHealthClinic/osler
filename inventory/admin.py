# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Drug)
class ViewAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DrugCategory)
class ViewAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MeasuringUnit)
class ViewAdmin(admin.ModelAdmin):
    pass

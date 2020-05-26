# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DrugCategory(models.Model):

    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return '{}'.format(self.name)


class MeasuringUnit(models.Model):

    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return '{}'.format(self.name)


class Drug(models.Model):

    name = models.CharField(max_length=100, blank=False)

    unit = models.ForeignKey(MeasuringUnit, blank=True, null=True)

    dose = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)

    total_inventory = models.PositiveSmallIntegerField(
        default=0, blank=True, null=True)

    category = models.ForeignKey(DrugCategory)

    def dose_empty(self):
        if dose == '':
            return True

    def __str__(self):
        return 'Category: {0}, Name: {1}, Unit:{2}, Dose: {3}, Total Inventory: {4}'.format(self.category, self.name, self.unit, self.dose, self.total_inventory)

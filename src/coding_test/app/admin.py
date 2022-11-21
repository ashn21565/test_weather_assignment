import json
# from code-challenge-template.src.coding_test.app.models import Weather

from django.http import HttpResponse
from django.contrib import admin
from django import forms
from django.shortcuts import render

from import_export.admin import ImportExportModelAdmin

from app.utils import ImportUtils
from app import models
# admin.site.register(models.AVGWeather)
# admin.site.register(models.Weather)

# class Average_weather_admin:
    
# Register your models here.

#station, date, max_temp, min_temp, ppt
class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class WeatherAdmin(admin.ModelAdmin):
    list_display = ("station", "date", "max_temp","min_temp","ppt")

admin.site.register(models.Weather, WeatherAdmin)

class AVGWeatherAdmin(admin.ModelAdmin):
    list_display = ("station", "date", "avg_max_temp","avg_min_temp","total_ppt")
admin.site.register(models.AVGWeather, AVGWeatherAdmin)

class YieldAdmin(admin.ModelAdmin):
    list_display = ("year","yield_value")
admin.site.register(models.Yield, YieldAdmin)
from django.contrib import admin

from bmi_log.models import BMI


@admin.register(BMI)
class BMIModelAdmin(admin.ModelAdmin):
    """
    Model admin for BMI Logs.
    """

    raw_id_fields = ['user']

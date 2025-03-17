from django.db import models
from django.contrib import admin
class Patient(models.Model):
    pat_name=models.CharField(max_length=30)
    pat_num=models.IntegerField(primary_key=True)
    doc_name=models.CharField(max_length=30)

class PatientAdmin(admin.ModelAdmin):
    list_display=('pat_name','pat_num','doc_name')

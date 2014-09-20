'''
Created on 20/09/2014

@author: abel
'''
from django.contrib import admin
from models import recibo
class recibo_admin(admin.ModelAdmin):
    pass
admin.site.register(recibo, recibo_admin)
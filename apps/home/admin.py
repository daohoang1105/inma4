# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin
from .models import Upload, User, AllSparePart, SparePartOutRecord, SparePartOutRequest
# Register your models here.

admin.site.register(User)
admin.site.register(Upload)
admin.site.register(SparePartOutRecord)
admin.site.register(SparePartOutRequest)
# admin.site.register(AllSparePart)

@admin.register(AllSparePart)
class AllSparePartAdmin(ImportExportActionModelAdmin):
    list_display = ('id','user' ,'partCode','goodStatus' ,'sparePartType' ,'csceHWMO' ,'serialNumber' ,'productDescription' ,'deliverDate','warehouse','sender','invoice','batch','transitWay','remark','actualQTY','consumQTY','remainQTY','updated','created')
    pass

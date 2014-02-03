from django.contrib import admin
from ajax_select import make_ajax_form
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django import forms
from django.utils.html import escape
from django.db.models import Count
from afsenai.models import Item, TakenItem, UserProfile

class TakenItemInline(admin.TabularInline):
	model = TakenItem
	extra = 1

class UserProfileAdmin(admin.ModelAdmin):
	search_fields = ['user__first_name', 'user__last_name', 'user__username', 'mispar_ishi']
	inlines = (TakenItemInline,)

class ItemAdmin(admin.ModelAdmin):
	inlines = (TakenItemInline,)

#admin.site.register(Hatima, HatimaAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
#admin.site.register(TakenItem)

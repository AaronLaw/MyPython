#coding:utf-8

from django.contrib import admin
from polls.models import *

class ChoiceInline(admin.TabularInline):#StackedInline):
	model = Choice
	extra = 5

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,{'fields':['pub_date']}),
		('Your Question',{'fields':['question']})
	]
	list_display = ('question','pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'
	inlines = [ChoiceInline]

admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
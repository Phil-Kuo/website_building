from django.contrib import admin

#yimin added
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
	def __unicode__(self):
		return self.list_display
	
# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)




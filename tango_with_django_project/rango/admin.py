from django.contrib import admin

#yimin added
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
	def __unicode__(self):
		return self.list_display
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page, PageAdmin)




from django.contrib import admin
from kategor.models import Categories

class CategoriesAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Categories._meta.fields]

	class Meta:
		model = Categories

admin.site.register(Categories, CategoriesAdmin)

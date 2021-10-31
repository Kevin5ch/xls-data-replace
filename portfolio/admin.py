from django.contrib import admin
from projects.models import Project, Category


# Cambiando el titulo del panel de administracion
admin.site.site_header = "Administración KSM"


# Modificando panel de administracion por modelos
class CategoryAdmin(admin.ModelAdmin):
  list_display = ("title","description","active")
  search_fields = ("title",)
  list_filter = ("active",)

class ProjectAdmin(admin.ModelAdmin):
  # ordering = ["-id"]
  list_display = ("title","content","status","public")
  search_fields = ("title",)
  list_filter = ("categories", "public", "created_at", "status")
  date_hierarchy = "created_at"
  save_as = True

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)

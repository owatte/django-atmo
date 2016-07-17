from django.contrib import admin
from atmogwada.models import IndiceAtmo

class IndiceAtmoAdmin(admin.ModelAdmin):
    date_hierarchy = 'record_date'

admin.site.register(IndiceAtmo, IndiceAtmoAdmin)

# Register your models here.

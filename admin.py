from django.contrib import admin
from atmogwada.models import IndiceAtmo

class IndiceAtmoAdmin(admin.ModelAdmin):
    u"""Use Admin only to visualize recorded data : the IndiceAtmo model
    appears read-only in the admin interface."""

    date_hierarchy = 'record_date'
    readonly_fields = []
    fields = ('today', 'tomorrow', 'date_today', 'config_date')

    def get_actions(self, request):
        u"""delete "action delete" from IndiceAtmo Admin."""
        actions = super(IndiceAtmoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        u"""Set fields as readonly."""
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields]

    def has_add_permission(self, request, obj=None):
        u"""forbid add action."""
        return False

    def has_delete_permission(self, request, obj=None):
        u"""forbid delete action"""
        return False

admin.site.register(IndiceAtmo, IndiceAtmoAdmin)

# Register your models here.

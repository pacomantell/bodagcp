from django.contrib import admin
from .models import MensajeContacto
# Register your models here.


@admin.action(description="Marcar como leídos")
def marcar_como_leido(modeladmin, request, queryset):
    queryset.update(estado="p")


@admin.action(description="Marcar como no leídos")
def marcar_como_no_leido(modeladmin, request, queryset):
    queryset.update(estado="d")


class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ("desc_nombre", "email", "desc_mensaje", "estado")
    fields = ["desc_nombre", "email", "desc_mensaje"]
    actions = [marcar_como_leido, marcar_como_no_leido]


admin.site.register(MensajeContacto, MensajeContactoAdmin)

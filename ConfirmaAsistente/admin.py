from django.contrib import admin
from .models import d_familia, d_contacto, fact_invitados, d_intolerancias
from contacto.models import MensajeContacto
from contacto.admin import MensajeContactoAdmin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from django.shortcuts import render

from .kpicalc import kpi_calc


# Invitado's actions
@admin.action(description="Desmarcar de nuevos")
def desmarcar_nuevo(modeladmin, request, queryset):
    queryset.update(estado="p")


@admin.action(description="Marcar como nuevo")
def marcar_nuevo(modeladmin, request, queryset):
    queryset.update(estado="d")


# Admin site override
class MyAdminSite(admin.AdminSite):
    site_header = 'Boda Francisco & Raquel'
    index_title = 'Administración'
    site_title = 'Boda F&R'

    # Main view
    def index(self, request, extra_context=None):
        app_list = self.get_app_list(request)

        # KPIs
        list_kpi = kpi_calc()

        context = {
            **self.each_context(request),
            "title": self.index_title,
            "subtitle": None,
            "app_list": app_list,
            "tot_inv": list_kpi[0],
            "kpi_veg": list_kpi[1],
            "kpi_ninio": list_kpi[2],
            "kpi_adultos": list_kpi[3],
            "kpi_mensajes": list_kpi[4],
            "kpi_no_leidos": list_kpi[5],
            "kpi_intol": list_kpi[6],
            "new_invitados": list_kpi[7],
            "kpi_veg_adult": list_kpi[8],
            "kpi_veg_nin": list_kpi[10],
            "kpi_intol_adult": list_kpi[9],
            "kpi_intol_nin": list_kpi[11],
            **(extra_context or {}),
        }
        return render(request, 'admin/dashboard.html', context)


admin_site = MyAdminSite(name="myadmin")


# Custom dropdown filter for contact
class ContactFilter(RelatedDropdownFilter):
    template = 'dropdown_filter.html'


class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre_contacto", "desc_email", "desc_telefono"]
    fields = ["nombre_contacto", "desc_email", "desc_telefono"]


class fact_invitadosAdmin(admin.ModelAdmin):
    list_display = ("desc_nombre", "id_contacto", "id_ninio", "id_vegetarian", "id_intolerancias", "id_familia", "estado")
    fields = ["desc_nombre", "id_ninio", "id_contacto", "id_vegetarian", "id_intolerancias", "id_familia"]
    list_filter = ["id_ninio", "id_vegetarian", "id_intolerancias", "id_familia", ("id_contacto", ContactFilter)]

    actions = [desmarcar_nuevo, marcar_nuevo]


class intoleranciasAdmin(admin.ModelAdmin):
    list_display = ["desc_intolerancias"]


admin.site.register(d_familia)
admin.site.register(d_contacto, ContactoAdmin)
admin.site.register(fact_invitados, fact_invitadosAdmin)
admin.site.register(d_intolerancias, intoleranciasAdmin)

admin_site.register(d_familia)
admin_site.register(d_contacto, ContactoAdmin)
admin_site.register(fact_invitados, fact_invitadosAdmin)
admin_site.register(MensajeContacto, MensajeContactoAdmin)
admin_site.register(d_intolerancias, intoleranciasAdmin)

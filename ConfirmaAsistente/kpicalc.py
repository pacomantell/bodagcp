from .models import fact_invitados, d_intolerancias
from contacto.models import MensajeContacto


def kpi_calc():
    tot_inv = fact_invitados.objects.count()
    kpi_veg = fact_invitados.objects.filter(id_vegetarian=2).count()
    kpi_ninio = fact_invitados.objects.filter(id_ninio=2).count()
    kpi_adultos = fact_invitados.objects.filter(id_ninio=1).count()
    kpi_mensajes = MensajeContacto.objects.count()

    new_invitados = fact_invitados.objects.filter(estado="d").count()

    kpi_intol = fact_invitados.objects.exclude(id_intolerancias=1).count()

    kpi_no_leidos = MensajeContacto.objects.filter(estado="d").count()
    kpi_veg_adult = fact_invitados.objects.filter(id_vegetarian=2, id_ninio=1).count()
    kpi_intol_adult = fact_invitados.objects.filter(id_ninio=1).exclude(id_intolerancias=1).count()

    kpi_veg_nin = kpi_veg - kpi_veg_adult
    kpi_intol_nin = kpi_intol - kpi_intol_adult

    return [
        tot_inv, kpi_veg, kpi_ninio, kpi_adultos,
        kpi_mensajes, kpi_no_leidos, kpi_intol, new_invitados,
        kpi_veg_adult, kpi_intol_adult, kpi_veg_nin, kpi_intol_nin]


def kpi_intol():
    kpi_tipo_int = {}
    for intolerancia in d_intolerancias.objects.all():
        # Only shows intolerancias
        if str(intolerancia) != "Nada":
            # KPis para cada intolerancia
            tipo_int = str(intolerancia)
            kpi_total = fact_invitados.objects.filter(id_intolerancias=d_intolerancias.objects.get(desc_intolerancias=intolerancia)).count()
            kpi_adulto = fact_invitados.objects.filter(id_intolerancias=d_intolerancias.objects.get(desc_intolerancias=intolerancia), id_ninio=1).count()
            kpi_nin = kpi_total - kpi_adulto
            # Only shows nonzero values
            if kpi_total != 0:
                kpi_tipo_int[tipo_int] = [kpi_total, kpi_adulto, kpi_nin]
    return kpi_tipo_int

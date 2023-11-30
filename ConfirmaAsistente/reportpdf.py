from .models import d_intolerancias, fact_invitados, d_familia
from .kpicalc import kpi_calc, kpi_intol

# PDF Generation imports
from io import BytesIO
from reportlab.lib import colors
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER


def report_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename=invitados.pdf'

    buffer = BytesIO()

    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

    doc = SimpleDocTemplate(buffer,
                            title="invitados.pdf",
                            rightMargin=1.5 * cm,
                            leftMargin=1.5 * cm,
                            topMargin=1 * cm,
                            bottomMargin=1 * cm,
                            pagesize=A4)
    w, h = A4
    # Styles
    styles = getSampleStyleSheet()
    # Kpi Titles
    styles.add(ParagraphStyle(name='CenterAlign', fontName='Helvetica', fontSize=12,
                              align=TA_CENTER))
    styles.add(ParagraphStyle(name='KpiRow', fontName='Helvetica', fontSize=12,
                              align=TA_CENTER, leftIndent=12))
    styles.add(ParagraphStyle(name='tableHeaders', fontName='Helvetica', fontSize=10,
                              align=TA_CENTER))
    styles.add(ParagraphStyle(name='tableRows', fontName='Helvetica', fontSize=10,
                              align=TA_JUSTIFY, leftIndent=12))
    styles.add(ParagraphStyle(name='tableRowsIntoler', fontName='Helvetica', fontSize=10,
                              align=TA_CENTER, leftIndent=24))
    # Invitados table style
    inv_table_style = TableStyle(
        [('LINEBELOW', (0, 0), (-1, -1), 1, colors.grey)]
    )

    # Container for elements
    elements = []

    # Title
    elements.append(Paragraph("INFORME GENERAL DE INVITADOS", style=styles['Heading1']))
    elements.append(Table([""], colWidths=(w - 2 * cm), style=inv_table_style))

    # Personal Data
    elements.append(Paragraph("Detalles del evento:", style=styles['Heading2']))
    elements.append(Paragraph("Nombre del evento: Boda Francisco y Raquel", style=styles['CenterAlign']))
    elements.append(Paragraph("Fecha del evento: 05/10/2024", style=styles['CenterAlign']))
    elements.append(Paragraph("Nombres clientes: Francisco José Mantell Zamudio, Raquel Uribe Enríquez", style=styles['CenterAlign']))
    elements.append(Paragraph("Contacto clientes: boda.franciscoyraquel@gmail.com", style=styles['CenterAlign']))
    elements.append(Paragraph("Lugar del evento: Jardines Alquería de la Vega (Purchil, Granada)", style=styles['CenterAlign']))
    elements.append(Paragraph("Catering: Catering Ibagar", style=styles['CenterAlign']))

    # HR Line
    elements.append(Table([""], colWidths=(w - 2 * cm), style=inv_table_style))

    elements.append(Paragraph("Información general:", style=styles['Heading2']))

    # KPIs
    list_kpi = kpi_calc()

    kpis = []

    kpis.append([Paragraph(" ", style=styles['CenterAlign']),
                 Paragraph("<b>Total</b>", style=styles['CenterAlign']),
                 Paragraph("<b>Adultos</b>", style=styles['CenterAlign']),
                 Paragraph("<b>Niños</b>", style=styles['CenterAlign'])])

    kpis.append([Paragraph("<b>Invitados: </b>", style=styles['CenterAlign']),
                 Paragraph(str(list_kpi[0]), style=styles['KpiRow']),
                 Paragraph(str(list_kpi[3]), style=styles['KpiRow']),
                 Paragraph(str(list_kpi[2]), style=styles['KpiRow'])])

    kpis.append([Paragraph("<b>Vegetarianos: </b>", style=styles['CenterAlign']),
                 Paragraph(str(list_kpi[1]), style=styles['KpiRow']),
                 Paragraph(str(list_kpi[8]), style=styles['KpiRow']),
                 Paragraph(str(list_kpi[10]), style=styles['KpiRow'])])

    kpis.append([Paragraph("<b>Intolerantes: </b>", style=styles['CenterAlign']),
                 Paragraph(str(list_kpi[6]), style=styles['KpiRow']),
                 Paragraph(str(list_kpi[9]), style=styles['KpiRow']),
                 Paragraph(str(list_kpi[11]), style=styles['KpiRow'])])

    t_kpi = Table(kpis)
    elements.append(t_kpi)
    elements.append(Spacer(1, 0.25 * cm))

    # KPIs tipos de intolerancias
    f_intolerancias = kpi_intol()
    kpi_tipo_int = []
    for intolerancia in list(f_intolerancias.keys()):
        # Only shows intolerancias
        kpi_tipo_int.append([
            Paragraph("<b>" + intolerancia + "</b>", style=styles['tableRowsIntoler']),
            Paragraph(str(f_intolerancias[intolerancia][0]), style=styles['tableRows']),
            Paragraph(str(f_intolerancias[intolerancia][1]), style=styles['tableRows']),
            Paragraph(str(f_intolerancias[intolerancia][2]), style=styles['tableRows'])
        ])

    tabla_int = Table(kpi_tipo_int)
    elements.append(tabla_int)
    elements.append(Spacer(1, 0.5 * cm))
    elements.append(Table([""], colWidths=(w - 2 * cm), style=inv_table_style))

    elements.append(Paragraph("Detalle de invitados por mesa:", style=styles['Heading2']))
    elements.append(Spacer(1, 0.5 * cm))

    # Tabla invitados
    for grupo in d_familia.objects.all().values():
        invitados = fact_invitados.objects.filter(id_familia=grupo['id_familia']).only("desc_nombre", "id_ninio", "id_vegetarian", "id_intolerancias").values()

        mesa = Paragraph("<b>· Mesa " + str(grupo['id_familia']) + " - " + str(grupo['flag_familia'] + ": " + str(invitados.count()) + "pax</b>"),
                         style=styles['CenterAlign'])
        elements.append(mesa)
        elements.append(Spacer(1, 0.25 * cm))
        data = []

        headers = [
            Paragraph("<b>Nombre y Apellidos</b>", style=styles['tableHeaders']),
            Paragraph("<b>Niño</b>", style=styles['tableHeaders']),
            Paragraph("<b>Vegetariano</b>", style=styles['tableHeaders']),
            Paragraph("<b>Intolerancias</b>", style=styles['tableHeaders']),
        ]

        data.append(headers)
        # Table rows
        for invitado in invitados:

            # Row formats
            if invitado["id_ninio_id"] == 1:
                invitado["id_ninio_id"] = " "
            else:
                invitado["id_ninio_id"] = "X"

            if invitado['id_vegetarian_id'] == 1:
                invitado["id_vegetarian_id"] = " "
            else:
                invitado["id_vegetarian_id"] = "X"

            # Row values
            name = str(invitado["desc_nombre"]).title()
            ninio = str(invitado["id_ninio_id"])
            vegetariano = invitado["id_vegetarian_id"]
            intol = str(d_intolerancias.objects.get(id_intolerancias=invitado["id_intolerancias_id"]))

            if intol == "Nada":
                intol = " "

            data.append([
                Paragraph(name, style=styles['tableRows']),
                Paragraph(ninio, style=styles['tableRows']),
                Paragraph(vegetariano, style=styles['tableRows']),
                Paragraph(intol, style=styles['tableRows'])
            ])

        t = Table(data, colWidths=[8.5 * cm, 2 * cm, 4 * cm, None], style=inv_table_style)
        elements.append(t)
        elements.append(Spacer(1, 0.75 * cm))

    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

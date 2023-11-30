from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email_confirmation(invitado, vegetariano):

    subject = 'BODA FRANCISCO & RAQUEL: CONFIRMACIÓN DE ASISTENCIA'
    to_email = invitado.cleaned_data['desc_email']
    from_email = "boda.franciscoyraquel@gmail.com"
    # cc = ["raqueluribeenriquez@gmail.com", "paco.mantell94@gmail.com"]    add to EmailMultiAlternatives

    context = {
        'name': invitado.cleaned_data['nombre_contacto'],
        'email': invitado.cleaned_data['desc_email'],
        'telefono': invitado.cleaned_data['desc_telefono'],
        'veg': vegetariano.cleaned_data['flag_vegetarian'],
        'intolerancias': invitado.cleaned_data['id_intolerancias']
    }
    html_context = render_to_string('email/email_contact.html', context)
    text_context = strip_tags(html_context)

    msg = EmailMultiAlternatives(subject, text_context, from_email, [to_email])
    msg.attach_alternative(html_context, "text/html")
    msg.send()


def send_email_acomp_confirmation(invitado, vegetariano, list_adultos, list_ninios):

    subject = 'BODA FRANCISCO & RAQUEL: CONFIRMACIÓN DE ASISTENCIA'
    to_email = invitado.cleaned_data['desc_email']
    from_email = "boda.franciscoyraquel@gmail.com"
    # cc = ["raqueluribeenriquez@gmail.com", "paco.mantell94@gmail.com"]   add to EmailMultiAlternatives

    context = {
        'name': invitado.cleaned_data['nombre_contacto'],
        'email': invitado.cleaned_data['desc_email'],
        'telefono': invitado.cleaned_data['desc_telefono'],
        'veg': vegetariano.cleaned_data['flag_vegetarian'],
        'intolerancias': invitado.cleaned_data['id_intolerancias'],
        'list_adultos': list_adultos,
        'list_ninios': list_ninios
    }
    html_context = render_to_string('email/email_inv_contact.html', context)
    text_context = strip_tags(html_context)

    msg = EmailMultiAlternatives(subject, text_context, from_email, [to_email])
    msg.attach_alternative(html_context, "text/html")
    msg.send()

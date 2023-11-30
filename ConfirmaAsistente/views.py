from django.http import HttpResponse
from django.shortcuts import render
from .models import d_familia, d_ninio, d_vegetariano, d_contacto, fact_invitados, d_intolerancias
from .forms import NumAcompForm, InvitadoForm, ContactConfForm, VegetarianoForm, IntoleranciasForm

from .email import send_email_confirmation, send_email_acomp_confirmation
from .reportpdf import report_pdf


def confirmation(request):

    # Vista inicial
    if request.method == 'GET':
        confirmation_contact_form = ContactConfForm()
        vegetariano_form = VegetarianoForm()
        num_acom = NumAcompForm()
        print('Vista Inicial')
        return render(request, 'confirmation.HTML', {
            'confirmation_contact_form': confirmation_contact_form, 'vegetariano_form': vegetariano_form,
            'num_acom': num_acom, 'nbar': 'confirmacion', 'flag_error': 'True'})

    #
    if request.method == 'POST':
        confirmation_contact_form = ContactConfForm(request.POST)
        vegetariano_form = VegetarianoForm(request.POST)
        num_acom = NumAcompForm(request.POST)

        # Valido que se ha introducido datos personales
        if confirmation_contact_form.is_valid() & vegetariano_form.is_valid():
            print('Contacto Introducido')

            if num_acom.is_valid():
                num_adult = num_acom.cleaned_data['num_adult']
                num_nin = num_acom.cleaned_data['num_nin']

                # Si el contacto no trae acompañantes lo guardamos directamente
                if (num_adult == 0) and (num_nin == 0):

                    print('Solo contacto')
                    confirmation_contact_form.save()

                    # Guardamos como invitado
                    invitado = fact_invitados(
                        desc_nombre=str(confirmation_contact_form.cleaned_data['nombre_contacto']).title(),
                        id_contacto=d_contacto.objects.get(desc_email=confirmation_contact_form.cleaned_data['desc_email']),
                        id_ninio=d_ninio.objects.get(flag_ninio='No'),
                        id_vegetarian=d_vegetariano.objects.get(id_vegetarian=vegetariano_form.cleaned_data['flag_vegetarian']),
                        id_intolerancias=d_intolerancias.objects.get(desc_intolerancias=confirmation_contact_form.cleaned_data['id_intolerancias']),
                        id_familia=d_familia.objects.get(flag_familia='Por Asignar'))
                    invitado.save()

                    # Si se ha introducido email enviamos confirmación
                    if confirmation_contact_form.cleaned_data['desc_email']:
                        send_email_confirmation(confirmation_contact_form, vegetariano_form)

                    print('Contacto guardado')
                    return render(request, 'success_confirmation.HTML', {'nbar': 'confirmacion'})

                # Si trae acompañantes pedimos sus datos
                else:
                    # Formulario invitados
                    if request.method == 'POST':
                        print('Vista acompañantes')
                        contact_form = ContactConfForm(request.POST)

                        list_adult = [i for i in range(1, int(num_adult) + 1)]
                        list_nin = [i for i in range(1, int(num_nin) + 1)]

                        inital_values = {
                            'desc_nombre': '',
                            'id_vegetarian': '',
                            'id_intolerancias': ''
                        }
                        list_acomp_adult_forms = [InvitadoForm(request.POST, inital_values) for i in list_adult]
                        list_acomp_nin_forms = [InvitadoForm(request.POST, inital_values) for i in list_nin]

                        # Validamos formulario de invitados
                        valid_inv_list = []
                        for i in list_acomp_adult_forms:
                            if i.is_valid():
                                valid = True
                                print('Adulto correcto')
                            else:
                                valid = False
                                print('Adulto incorrecto')
                            valid_inv_list.append(valid)
                        for i in list_acomp_nin_forms:
                            if i.is_valid():
                                valid = True
                                print('Niño correcto')
                            else:
                                valid = False
                                print('Niño incorrecto')
                            valid_inv_list.append(valid)

                        if all(valid_inv_list) is True:
                            print('Formulario acompañante correcto')
                            confirmation_contact_form.save()

                            print('Contacto guardado vista acompañantes')

                            # Guardamos los adultos
                            list_acomp_adult = []
                            for adult in list_acomp_adult_forms:

                                invitado = fact_invitados(
                                    desc_nombre=str(adult.cleaned_data['desc_nombre']).title(),
                                    id_contacto=d_contacto.objects.get(desc_email=confirmation_contact_form.cleaned_data['desc_email']),
                                    id_ninio=d_ninio.objects.get(flag_ninio='No'),
                                    id_vegetarian=adult.cleaned_data['id_vegetarian'],
                                    id_intolerancias=d_intolerancias.objects.get(desc_intolerancias=adult.cleaned_data['id_intolerancias']),
                                    id_familia=d_familia.objects.get(flag_familia='Por Asignar')
                                )
                                invitado.save()
                                list_acomp_adult.append(invitado)
                                print('Adulto Guardado')
                            # Guardamos los ninios
                            list_acomp_nin = []
                            for ninio in list_acomp_nin_forms:

                                invitado = fact_invitados(
                                    desc_nombre=str(ninio.cleaned_data['desc_nombre']).title(),
                                    id_contacto=d_contacto.objects.get(desc_email=confirmation_contact_form.cleaned_data['desc_email']),
                                    id_ninio=d_ninio.objects.get(flag_ninio='Si'),
                                    id_vegetarian=ninio.cleaned_data['id_vegetarian'],
                                    id_intolerancias=ninio.cleaned_data['id_intolerancias'],
                                    id_familia=d_familia.objects.get(flag_familia='Por Asignar')
                                )
                                invitado.save()
                                list_acomp_nin.append(invitado)
                                print('Ninio Guardado')

                            # Guardamos el contacto como invitado
                            invitado = fact_invitados(
                                desc_nombre=str(confirmation_contact_form.cleaned_data['nombre_contacto']).title(),
                                id_contacto=d_contacto.objects.get(desc_email=confirmation_contact_form.cleaned_data['desc_email']),
                                id_ninio=d_ninio.objects.get(flag_ninio='No'),
                                id_vegetarian=d_vegetariano.objects.get(id_vegetarian=vegetariano_form.cleaned_data['flag_vegetarian']),
                                id_intolerancias=d_intolerancias.objects.get(desc_intolerancias=confirmation_contact_form.cleaned_data['id_intolerancias']),
                                id_familia=d_familia.objects.get(flag_familia='Por Asignar'))
                            invitado.save()

                            # Email de confirmación
                            if confirmation_contact_form.cleaned_data['desc_email'] != "-":
                                send_email_acomp_confirmation(confirmation_contact_form, vegetariano_form, list_acomp_adult, list_acomp_nin)
                            # Pantalla de confirmacion
                            print('Formulario completado')
                            return render(request, 'success_confirmation.HTML', {'nbar': 'confirmacion'})
                        else:
                            print('Formulario acompañante incorrecto')
                            return render(request, 'form_confirmation.html', {
                                'contact_form': contact_form, 'list_acomp_adult_forms': list_acomp_adult_forms,
                                'list_acomp_nin_forms': list_acomp_nin_forms, 'num_acom': num_acom,
                                'num_adul': num_adult, 'num_nin': num_nin, 'nbar': 'confirmacion',
                                'vegetariano_form': vegetariano_form})
                    else:
                        # Pantalla de error
                        return HttpResponse("Método erróneo")

            else:
                return render(request, 'confirmation.HTML', {
                    'confirmation_contact_form': confirmation_contact_form, 'num_acom': num_acom,
                    'nbar': 'confirmacion', 'flag_error': 'True'})
        else:
            print('Contacto no válido')
            return render(request, 'confirmation.HTML', {
                'confirmation_contact_form': confirmation_contact_form, 'num_acom': num_acom,
                'nbar': 'confirmacion', 'flag_error': 'False'})

# Export to PDF


def export_to_pdf(request):
    return report_pdf(request)

from django.shortcuts import render
from .forms import ContactForm
from django.views import View


# Vista Inicial
class PlayListView(View):
    def get(self, request):
        return render(request, 'playlist.HTML', {'nbar': 'bienvenido'})


# Vista contacto
class ContactView(View):

    def get(self, request):
        contact_form = ContactForm()
        return render(request, 'contact.HTML', {'contact_form': contact_form, 'nbar': 'contactform'})

    def post(self, request):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():

            # Guardamos mesaje
            contact_form.save()

            return render(request, 'success.HTML', {'nbar': 'contactform'})
        else:
            return render(request, 'contact.HTML', {'contact_form': contact_form, 'nbar': 'contactform'})

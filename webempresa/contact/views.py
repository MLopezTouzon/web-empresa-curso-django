from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",  # Iria el de la empresa que tiene que concordar con el dominio
                ["pa_co_89@hotmail.com"],
                reply_to=[email]
            )
            try:
                # email.send()
                return redirect(reverse('contact')+"?ok")  # Todo fue bien, redireccionamos a OK
            except Exception as e:       # El except solo me da aviso de que puedes especificar guardar la excepción de forma extensa, por ejemplo, e será un objeto con información de la excepción genérica.
                return redirect(reverse('contact')+"?fail")  # Algo no ha ido bien, redireccionamos a FAIL

    return render(request, "contact/contact.html", {'form': contact_form})

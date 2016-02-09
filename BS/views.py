from braces.views import JSONResponseMixin, AjaxResponseMixin
from django.http import HttpResponse
from django.views import generic


#from django.core.mail import EmailMessage
#from .e_mail import sendmail



class Index(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        return context


class Contacts(generic.TemplateView):
    template_name = 'contact.html'


class ReservationForm(generic.TemplateView):
    template_name = 'reservation-form.html'


class Reservation(generic.View,JSONResponseMixin, AjaxResponseMixin):
    content_type = 'application/javascript'

    def post(self, request, *args, **kwargs):
#        try:
#            album = Album.objects.get(slug=kwargs.get('slug'))
#        except Album.DoesNotExist:
#            error_dict = {'message': 'Album not found.'}
#            return self.render_json_response(error_dict, status=404)

#        uploaded_file = request.FILES['images']
#        Photo.objects.create(album=album, file=uploaded_file, description=uploaded_file.name)
#        response_dict = {'message': 'File uploaded successfully!', }

        #sendmail('sergeii_@mail.ru','test','boby')
       # email = EmailMessage('Test', 'Test body', to=['sergeii_@mail.ru'])
       # email.send()
        rez="<p class='c-alert-message m-success'>Ваша заявка успешно отправлена.</p>"
        return HttpResponse(rez)


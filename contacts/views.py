from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail, send_mass_mail
from django.shortcuts import render
import django_rq
from contacts.forms import ContactPostForm



def contacts(request):
    if request.method == 'GET':
        form = ContactPostForm(request.GET)
        return render(request, 'contacts/contact_form.html', {'form': form})
    if request.method == 'POST':
        form = ContactPostForm(request.POST)
        if form.is_valid():
            subject = 'Заявка с сайта'
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['user_email']
            host_email = 'pnirtep@gmail.com'
            message = form.cleaned_data['message']
            to_message = '{}, ваша заявка принята, мы свяжемся с вами в течени 24 часов'.format(name)
            # send_mail(subject, message, user_email, [host_email], fail_silently=False)
            # send_mail(subject, to_message, host_email, [user_email], fail_silently=False)
            queue = django_rq.get_queue('default')
            queue.enqueue(send_mail, subject, message, user_email, [host_email])
            queue.enqueue(send_mail, subject, to_message, EMAIL_HOST_USER, [user_email])
            # message1 = (subject, message, user_email, [host_email])
            # message2 = (subject, to_message, EMAIL_HOST_USER, [user_email])
            # send_mass_mail((message1, message2), fail_silently=False)
            return render(request, 'contacts/contact_form_thanks.html')

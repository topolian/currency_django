from currency.models import ContactUs, Rate
from currency.utils import generate_password as gen_pass

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)


def contacts_list(request):
    contacts = ContactUs.objects.all()

    context = {
        'contacts_list': contacts
    }
    # result = []
    # for contact in contacts:
    #     result.append(
    #         f'Id: {contact.id}; From: {contact.email_from}; Subject: {contact.subject}; Message: {contact.message}</br>'
    #     )
    return render(request, 'contacts.html', context=context)


def rate_list(request):
    rates = Rate.objects.all()

    context = {
        'rate_list': rates
    }

    return render(request, 'rate_list.html', context=context)

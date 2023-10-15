from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source
from currency.utils import generate_password as gen_pass

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView,
    DeleteView
)
from django.urls import reverse_lazy


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


# def rate_list(request):
#     rates = Rate.objects.all()
#
#     context = {
#         'rate_list': rates
#     }
#
#     return render(request, 'rate_list.html', context=context)

class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'

# def rate_create(request):
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('rate-list')
#     elif request.method == 'GET':
#         form = RateForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'rate_create.html', context=context)


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


# def rate_details(request, rate_id):
#     rate = get_object_or_404(Rate, id=rate_id)
#     context = {
#         'object': rate
#     }
#     return render(request, 'rate_details.html', context=context)

class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


# def rate_update(request, rate_id):
#     rate = get_object_or_404(Rate, id=rate_id)
#     if request.method == 'POST':
#         form = RateForm(request.POST, instance=rate)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list')
#     elif request.method == 'GET':
#         form = RateForm(instance=rate)
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'rate_update.html', context=context)

class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


# def rate_delete(request, rate_id):
#     rate = get_object_or_404(Rate, id=rate_id)
#
#     if request.method == 'POST':
#         rate.delete()
#         return HttpResponseRedirect('/rate/list')
#     context = {
#         'object': rate
#     }
#     return render(request, 'rate_delete.html', context=context)

class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_create.html'


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_delete.html'

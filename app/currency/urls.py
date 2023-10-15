from currency.views import (
    contacts_list, generate_password,
    RateCreateView, RateDeleteView,
    RateDetailView, RateListView, RateUpdateView, SourceCreateView,
    SourceDeleteView, SourceDetailView, SourceListView,
    SourceUpdateView)

from django.urls import path

app_name = 'currency'

urlpatterns = [

    path('gen-pass/', generate_password),
    path('contacts/list/', contacts_list, name='contacts-list'),
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),

]

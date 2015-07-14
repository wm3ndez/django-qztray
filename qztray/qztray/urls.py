from django.conf.urls import url
from django.views.generic import TemplateView
from views import sign_printer_request

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^sign-printer-request/$', sign_printer_request, name='sign-printer-request'),
]

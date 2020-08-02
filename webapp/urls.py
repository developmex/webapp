"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from transporte.views import IndexView, login, logout, CustomerListView, dashboard, GeneratePdf, CustomerCreateView, CustomerDetailView, ServiceListView, InvoiceListView
admin.site.site_header = 'Valley Administrator'
admin.site.site_title = 'Valley Medical Transport'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pdf/', GeneratePdf.as_view()),
    url(r'^customers/view/(?P<pk>[0-9]+)/$', CustomerDetailView.as_view(), name='customer-detail'),

    url(r'customer/add/$', CustomerCreateView.as_view(), name='customer_add'),
    url(r'^$', IndexView.as_view(), {'redirect_if_logged_in': '/dashboard/'}, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^customers/list/', CustomerListView.as_view(), name='customerlistview'),
    url(r'^services/list/', ServiceListView.as_view(), name='servicelistview'),
    url(r'^invoices/list/', InvoiceListView.as_view(), name='invoicelistview'),
]

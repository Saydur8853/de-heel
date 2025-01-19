from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('product/<int:id>/', product_details, name='product_details'),
    path('submit-appointment/', submit_appointment, name='submit_appointment'), 
    path('submit-company-inquiry/', submit_company_inquiry, name='submit_company_inquiry'),
    path('mark-appointment-as-viewed/<int:appointment_id>/', mark_appointment_as_viewed, name='mark_appointment_as_viewed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
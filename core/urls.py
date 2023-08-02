from django.urls import path

from .views import AboutUsView, ContactInformationView

urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('about-us/edit/', AboutUsView.as_view(), name='about-us-edit'),
    path('contact-information/', ContactInformationView.as_view(), name='contact-information'),
    path('contact-information/create/', ContactInformationView.as_view(), name='contact-information-create'),

]

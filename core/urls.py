from django.urls import path

from .views import AboutUsView, ContactInformationView, ContactInformationListView  ,ProductDetailView, ProductView, ProductListView, TestimonialView, TestimonialDetailView

urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('about-us/edit/', AboutUsView.as_view(), name='about-us-edit'),

    path('contact-information/', ContactInformationView.as_view(), name='contact-information'),
    path('contact-information/create/', ContactInformationView.as_view(), name='contact-information-create'),
    path('contact-information/edit/', ContactInformationView.as_view(), name='contact-information-edit'),
    path('contact-information/list/', ContactInformationListView.as_view(), name='contact-information-list'),

    path('products/list/', ProductListView.as_view(), name='products-list'),
    path('products/create/', ProductView.as_view(), name='products-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products-detail'),
    path('products/<int:pk>/edit/', ProductDetailView.as_view(), name='products-detail-edit'),
    path('products/<int:pk>/delete/', ProductDetailView.as_view(), name='products-detail-delete'),

    path('testimonials/', TestimonialView.as_view(), name='testimonials'),
    path('testimonials/create/', TestimonialView.as_view(), name='testimonials-create'),
    path('testimonials/<int:pk>/', TestimonialDetailView.as_view(), name='testimonial-detail'),
    path('testimonials/<int:pk>/edit/', TestimonialDetailView.as_view(), name='testimonial-detail-edit'),
    path('testimonials/<int:pk>/delete/', TestimonialDetailView.as_view(), name='testimonial-detail-delete'),

]

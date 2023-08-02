from django.urls import path

from .views import AboutUsView, ContactInformationView, ContactInformationListView  ,ProductDetailView, ProductView, ProductListView, TestimonialView, TestimonialDetailView, TestimonialListView, ServiceView, ServiceDetailView, ServiceListView, BlogPostView, BlogPostDetailView, BlogPostListView

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
    path('testimonials/list/', TestimonialListView.as_view(), name='testimonials-list'),


    path('services/', ServiceView.as_view(), name='services'),
    path('services/create/', ServiceView.as_view(), name='services-create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='services-detail'),
    path('services/<int:pk>/edit/', ServiceDetailView.as_view(), name='services-detail-edit'),
    path('services/<int:pk>/delete/', ServiceDetailView.as_view(), name='services-detail-delete'),
    path('services/list/', ServiceListView.as_view(), name='services-list'),

    path('blog-posts/', BlogPostView.as_view(), name='blog-posts'),
    path('blog-posts/create/', BlogPostView.as_view(), name='blog-posts-create'),
    path('blog-posts/<int:pk>/', BlogPostDetailView.as_view(), name='blog-posts-detail'),
    path('blog-posts/<int:pk>/edit/', BlogPostDetailView.as_view(), name='blog-posts-detail-edit'),
    path('blog-posts/<int:pk>/delete/', BlogPostDetailView.as_view(), name='blog-posts-detail-delete'),
    path('blog-posts/list/', BlogPostListView.as_view(), name='blog-posts-list'),


]

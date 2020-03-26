from django.contrib.staticfiles.views import serve
from django.urls import path
from . import views
from .views import HomeView, EntryView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry-detail'),
    path('about/', AboutView.as_view(), name='blog-about'),
    path('contact.html', views.contact, name='blog-contact'),


]

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name="detail"),
    path("<int:id>/results", views.results, name="results"),
    path("create_item/", views.create_item, name="create_item"),
    path('image_upload', views.hotel_image_view, name = 'image_upload'),
    path('success/', views.success, name = 'success'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('login/', views.LoginUser.as_view(), name = 'login'),
]

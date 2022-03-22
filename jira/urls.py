from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name="general"),
    path('login/', views.create, name="login"),
    path('templates/google/', views.google_sheet, name="google_sheet"),
    path('templates/google2/', views.google_sheet2, name="google_sheet"),
    path('templates/google2/<str:login>/', views.google_sheet2, name="google_sheet"),
    path('templates/google2/<str:login>/<str:password>', views.google_sheet2, name="google_sheet")
    
]
from django.urls import path 
from . import views
from .views import organization_create_view, blood_detail_create_view, login

urlpatterns = [
    path('', organization_create_view, name='organization_create'),  # Comma added here
    path('blood_detail/create/',views.blood_detail_create_view, name='blood_detail_create'),
    path('login/',views.login,name='login')
]

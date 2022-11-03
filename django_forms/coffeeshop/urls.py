from django.urls import path

from . import views
app_name = 'coffeeshop'

urlpatterns = [
    path('', views.home, name='home'),
    path('thanks/', views.thanks, name='thanks'),
    path('signup/', views.signup, name='signup'),
    path('details/', views.details, name='details'),
]
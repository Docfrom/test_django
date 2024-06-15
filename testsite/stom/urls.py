from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    # path('serv/<int:serv_id>/', views.service, name='service'),
    path('serv/', views.service, name='service'),
    # path('doc/<slug:docsl>/', views.doctors, name='doctor'),
    path('doc/', views.doctors, name='doctor'),
    path('archive/<year4:year>/', views.archive, name='archive'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('login/', views.login, name='login')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('log/', views.login_view, name='log'),
    path('deluser/', views.deluser, name='deluser'),
    path('history/', views.history, name='history'),
    path('history/delete/<int:sno>/', views.delete, name='delete'),
]

from . import views
from django.urls import path

urlpatterns = [
    path('',views.fun,name='fun'),
    path('add',views.add,name='add'),
    path('add/', views.add_product, name='add_product')

    ]
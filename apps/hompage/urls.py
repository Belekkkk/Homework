from django.urls import path

from apps.hompage import views


urlpatterns = [
    path('',views.index, name='hompages'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.retrieve, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.destroy, name='destroy'),


]
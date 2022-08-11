from django.urls import path
from pokemon import views


urlpatterns = [

    path('type/', views.RegisterTipoView.as_view(), name='type'),

    path('type/<int:pk>/', views.RegisterTipoDetailView.as_view()),

    path('pokemon/', views.RegisterPersonajeView.as_view(), name='pokemon'),

    path('pokemon/<int:pk>/', views.RegisterPersonajeDetailView.as_view()),

]
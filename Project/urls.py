
from django.contrib import admin
from django.urls import path
from Etudiant import views

urlpatterns = [
    path('Etudiant_Inscrits/', views.Etudiant_Inscrits, name = 'Etudiant_Inscrits' ),
    path('admin/', admin.site.urls),
    path('', admin.site.urls, name = 'Admin'),
    path('Inscription/', views.Inscription, name = 'Inscription' ),
    path('update_Etudiant/<str:pk>/', views.update_Etudiant, name = 'update_Etudiant' ),
    path('delete_etudiant/<str:pk>/', views.delete_etudiant, name = 'delete_etudiant' ),
]

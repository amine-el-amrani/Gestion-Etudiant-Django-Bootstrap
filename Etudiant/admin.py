from django.contrib import admin
from .models import *
from .forms import EtudiantForm


class AdminForm1(admin.ModelAdmin):
    list_display = ['NOM', 'Prenom', 'Email', 'Date_de_naissance', 'Lieu_de_naissance', 'Statut', 'Cours']
    form = EtudiantForm
    list_filter = ['NOM']
    search_fields = ['NOM', 'Statut']


admin.site.register(Etudiant, AdminForm1)
admin.site.register(Statut)
admin.site.register(Cours )
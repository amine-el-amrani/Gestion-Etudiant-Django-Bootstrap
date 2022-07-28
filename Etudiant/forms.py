from django import forms
from .models import Etudiant, Cours


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['NOM',
        'Prenom',
        'Email', 
        'Date_de_naissance',
         'Lieu_de_naissance', 
         'Statut',
         'Cours']
    def clean_Email(self):
        Email = self.cleaned_data.get('Email')
        if not Email :
            raise forms.ValidationError('This field is required')
        for instance in Etudiant.objects.all():
            if instance.Email == Email:
                raise forms.ValidationError('The student is already saved')
        return Email

class EtudiantSearchForm(forms.ModelForm):
    export_to_csv = forms.BooleanField(required=False)
    class Meta:
        model = Etudiant
        fields =  ['NOM', 'Email']

class EtudiantUpdateForm(forms.ModelForm):
    class Meta :
        model = Etudiant
        fields = ['NOM',
        'Prenom',
        'Email', 
        'Date_de_naissance',
         'Lieu_de_naissance', 
         'Statut', 'Cours']
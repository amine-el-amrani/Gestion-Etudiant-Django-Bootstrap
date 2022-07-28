from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
import csv
from django.contrib import messages

def Home(request):
    title = 'Welcome to my Page'
    form = 'Welcome to my Page'
    context = {
        "title" : title,
        "test" : form,
    }
    return render (request, "Home.html",context)
    
def Etudiant_Inscrits(request):
    title = "Etudiant Inscrits"
    header = "Etudiant Inscrits"
    form = EtudiantSearchForm(request.POST or None)
    queryset = Etudiant.objects.all()
    context = {
        "title" : title,
        "queryset" : queryset,
        "header" : header,
        "form" : form,
    }
    if request.method == 'POST':
        queryset = Etudiant.objects.filter(NOM__icontains=form['NOM'].value(),
        Email__icontains=form['Email'].value(
        ))
        if form['export_to_csv'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] ='attachment ; filename = "Etudiant Inscrits.csv"'
            writer = csv.writer(response)
            writer.writerow(['NOM','Prenom','Email','Date_de_naissance','Lieu_de_naissance', 'Statut', 'Cours'])
            instance = queryset
            for obj in instance :
                writer.writerow([obj.NOM, obj.Prenom, obj.Email, obj.Date_de_naissance, obj.Lieu_de_naissance, obj.Statut])
            return response
        context = {
        "form" : form,
        "header" : header,
        "queryset" : queryset,
    }
    
    return render(request, "Etudiant_Inscrits.html",context)


def Inscription(request):
    header = "Inscription"
    form = EtudiantForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/Inscription')
    context = {
        "form" : form,
        "title" : "Inscription",
        "header" : header,
    }
    return render(request, "inscription.html", context)
        
def update_Etudiant(request, pk):
    queryset = Etudiant.objects.get(id=pk)
    form = EtudiantUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = EtudiantUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/Etudiant_Inscrits')
    context = {
        'form' : form
    }
    return render(request, 'inscription.html',context)

def delete_etudiant(request, pk):
    queryset = Etudiant.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Saved')
        return redirect('/Etudiant_Inscrits')
    return render(request, 'delete_etudiant.html')
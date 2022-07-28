from django.db import models

Statut_choice = {
    ('Etudiant', 'Etudiant'),
    ('Professeur', 'Professeur'),
    ( 'MCF', 'MCF'),
    ('VAC_EXT', 'VAC_EXT'),
    ('VAC_INT', 'VAC_INT'),
}

Cours_choice = {
    ('Programation', 'Programation'),
    ('Réseaux', 'Réseaux'),
    ( 'SQL', 'SQL'),
    ('Java', 'Java'),
    ('Python', 'Python'),
}
class Statut(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

class Cours(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    salle = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name


class Etudiant(models.Model):
    NOM = models.CharField(max_length=200, blank=True, null=True)
    Prenom = models.CharField(max_length=200,blank=True, null=True)
    Email = models.EmailField(max_length=200, blank=True, null=True)
    Date_de_naissance = models.DateField('date de naissance')
    Lieu_de_naissance = models.CharField(max_length=200, blank=False, null=False)
    Statut =models.ForeignKey(Statut, on_delete=models.CASCADE, blank = False)
    Cours =models.ForeignKey(Cours, on_delete=models.CASCADE, blank = False)

def __str__(self):
    return self.Etudiant_NOM
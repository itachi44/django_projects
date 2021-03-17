from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class MarqueVoiture(models.Model):
    RENAULT = 'RENAULT'
    PEUGEOT = 'PEUGEOT'
    VOLKSWAGEN = 'VOLKS'
    CITROEN = 'CITROEN'
    MERCEDES_BENZ = 'MB'
    OPEL = "OPEL"
    BMW = "BMW"
    FORD = "FORD"

    MARQUES = [
        (RENAULT, 'RENAULT'),
        (PEUGEOT, 'PEUGEOT'),
        (VOLKSWAGEN, 'VOLKSWAGEN'),
        (OPEL, 'OPEL'),
        (CITROEN, 'CITROEN'),
        (MERCEDES_BENZ, 'MERCEDEZ_BENZ'),
        (BMW, 'BMW'),
        (FORD, 'FORD'),
        # non exhaustif
    ]

    marques = models.CharField(max_length=25, choices=MARQUES)

    def __str__(self):
        return self.marques


def current_year():
    return datetime.date.today().year


class Annee(models.Model):
    annee = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1980), MaxValueValidator(current_year())])


class ModeleVoiture(models.Model):
    MODELES = []
    modele_label = models.CharField(max_length=25, choices=MODELES)
    annee = models.ForeignKey(Annee, related_name='modele', default=2021, on_delete=models.DO_NOTHING)
    marque = models.ForeignKey(MarqueVoiture, related_name='marque', default=datetime.date.today().year, on_delete=models.RESTRICT)

    def __str__(self):
        return self.modele_label


class CategoriePiece(models.Model):
    categorie_name = models.CharField(max_length=100)
    # ManyToMany (table ad hoc)

    categorie_modele = models.ManyToManyField(ModeleVoiture, default=None, related_name='categoriePiece', blank=True)

    def __str__(self):
        return self.categorie_name


class PieceVoiture(models.Model):
    label_piece = models.CharField(max_length=200, unique=True)
    prix_piece = models.FloatField(null=False)
    desc_piece = models.CharField(max_length=1024)
    categorie = models.ForeignKey(CategoriePiece, default=1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.label_piece


class LigneCommande(models.Model):
    prix_piece = models.FloatField(null=False)
    qte = models.IntegerField(null=False, default=1)
    pieceVoiture = models.ForeignKey(PieceVoiture, related_name='ligneCommande', on_delete=models.CASCADE)


class Client(models.Model):
    nom_client = models.CharField(max_length=50)
    prenom_client = models.CharField(max_length=50)
    tel_client = models.CharField(max_length=15)

    def __str__(self):
        all_name = self.nom_client + " " + self.prenom_client
        return all_name



class Commande(models.Model):
    date_commande = models.DateTimeField(auto_now_add=True)
    montant_total = models.FloatField(null=False)
    # nouvelle table ad hoc
    # foreign key ligne de commandes
    ligneCommande = models.ForeignKey(LigneCommande, related_name='commande', on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, related_name='commande', on_delete=models.DO_NOTHING)


class CompteClient(models.Model):
    email_client = models.EmailField(max_length=100)
    mdp_client = models.CharField(max_length=50, unique=True)
    client = models.OneToOneField(Client, related_name='compte', on_delete=models.CASCADE)

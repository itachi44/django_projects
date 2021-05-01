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

    marques = models.CharField(max_length=50, choices=MARQUES)

    def __str__(self):
        return self.marques


def current_year():
    return datetime.date.today().year


class ModeleVoiture(models.Model):
    RENAULT_ARKANA = 'REANAULT ARKANA'
    RENAULT_CLIO = 'RENAULT CLIO'
    RENAULT_ESPACE = 'RENAULT ESPACE'
    RENAULT_KADJAR = 'RENAULT KADJAR'
    RENAULT_KOLEOS = 'RENAULT KOLEOS'
    FORD_ECOSPORT = 'FORD ECOSPORT'
    FORD_EXPLORER = 'FORD EXPLORER'
    FORD_F150 = 'FORD_F150'
    FORD_FIESTA = 'FORD FIESTA'
    FORD_EXPOSITION = 'FORD EXPOSITION'
    FORD_FOCUS = 'FORD FOCUS'
    FORD_GALAXY = 'FORD GALAXY'
    BMW_SERIE1 = 'BMW SERIE 1'
    BMW_M135IXDRIVE = 'BMW M135i XDrive'
    BMW_X1 = 'BMW X1'
    BMW_X2 = 'BMW X2'
    BMW_X2_M35I = 'BMW X2 M35i'
    BMW_I3 = 'BMW i3'
    BMW_X6 = 'BMW X6'

    MODELES = [
        (RENAULT_ARKANA, 'REANAULT ARKANA'),
        (RENAULT_CLIO, 'RENAULT CLIO'),
        (RENAULT_ESPACE, 'RENAULT ESPACE'),
        (RENAULT_KADJAR, 'RENAULT KADJAR'),
        (RENAULT_KOLEOS, 'RENAULT KOLEOS'),
        (FORD_ECOSPORT, 'FORD ECOSPORT'),
        (FORD_EXPLORER, 'FORD EXPLORER'),
        (FORD_F150, 'FORD_F150'),
        (FORD_FIESTA, 'FORD FIESTA'),
        (FORD_EXPOSITION, 'FORD EXPOSITION'),
        (FORD_FOCUS, 'FORD FOCUS'),
        (FORD_GALAXY, 'FORD GALAXY'),
        (BMW_SERIE1, 'BMW SERIE 1'),
        (BMW_M135IXDRIVE, 'BMW M135i XDrive'),
        (BMW_X1, 'BMW X1'),
        (BMW_X2, 'BMW X2'),
        (BMW_X2_M35I, 'BMW X2 M35i'),
        (BMW_I3, 'BMW i3'),
        (BMW_X6, 'BMW X6'),
    ]

    modele_label = models.CharField(max_length=25, choices=MODELES)
    annee = models.PositiveIntegerField(default=current_year(),
                                        validators=[MinValueValidator(1980), MaxValueValidator(current_year())])
    marque = models.ForeignKey(MarqueVoiture, related_name='marque',
                               on_delete=models.RESTRICT)

    def __str__(self):
        return self.modele_label


class Motorisation(models.Model):
    DIESEL = 'DIESEL'
    GPL = 'GPL'
    HYBRIDE = 'HYBRIDE'
    ESSENCE = 'ESSENCE'
    E85 = 'E85'

    MOTORISATION = [
        (DIESEL, 'DIESEL'),
        (GPL, 'GPL'),
        (HYBRIDE, 'HYBRIDE'),
        (ESSENCE, 'ESSENCE'),
        (E85, 'E85'),
    ]

    motorisation = models.CharField(max_length=100, choices=MOTORISATION)
    modele_label = models.ForeignKey(ModeleVoiture, related_name='modele', on_delete=models.CASCADE)


class CategoriePiece(models.Model):
    # Pièces détachées
    ENT_ET_TRANS = 'ENTRAINEMENT ET TRANSMISSION'
    FREINS = 'FREINS'
    AME_INT = 'AMENAGEMENTS INTERIEURS'
    MOTEURS = 'MOTEURS ET PIECES DE MOTEUR'
    ES_LA_GLACE = 'Essuie-glaces / Lave-glaces'
    FILTRES = 'FILTRES'
    CAPTEURS = 'CAPTEURS'
    ALLUMAGE = 'ALLUMAGE'
    ECHA_SYST = 'ECHAPPEMENT ET SYSTEME D\'ECHAPPEMENT'
    DIRECT_SUSPEN = 'DIRECTION ET SUSPENSION'
    BATTERIES = 'BATTERIES'

    # Accessoires
    PORT_BAG = 'PORTE-BAGAGES ARRIÈRE'
    GAL_TOIT_COFFRES = 'CALERIES DE TOIT ET COFFRES'
    PNEUS_JANTES = 'PNEUS ET JANTES'
    ATT_REMORQUE = 'ATTELAGES POUR REMORQUE'
    ACCESS_PNEUS = 'ACCESSOIRES PNEUS ET JANTES'
    OUTILS = 'OUTILS'
    ENTRE_PNEUS = 'ENTRETIEN DES PNEUS'
    ENTRE_JANTES = 'ENTRETIEN DES JANTES'
    ENTRE_INTER = 'ENTRETIEN INTERIEUR'
    ENTRE_MOTEUR = 'ENTRETIEN MOTEUR'
    VOLANTS = 'VOLANTS ET MOYEUX DE VOLANTS'
    ASSIST_PANNE = 'ASSISTANCE PANNE'
    EPON_CHIF_BROS = 'EPONGES, CHIFFON, BROSSES'

    CATEGORIES = [
        (ENT_ET_TRANS, 'ENTRAINEMENT ET TRANSMISSION'),
        (ENT_ET_TRANS, 'ENTRAINEMENT ET TRANSMISSION'),
        (FREINS, 'FREINS'),
        (AME_INT, 'AMENAGEMENTS INTERIEURS'),
        (MOTEURS, 'MOTEURS ET PIECES DE MOTEUR'),
        (ES_LA_GLACE, 'Essuie-glaces / Lave-glaces'),
        (FILTRES, 'FILTRES'),
        (CAPTEURS, 'CAPTEURS'),
        (ALLUMAGE, 'ALLUMAGE'),
        (ECHA_SYST, 'ECHAPPEMENT ET SYSTEME D\'ECHAPPEMENT'),
        (DIRECT_SUSPEN, 'DIRECTION ET SUSPENSION'),
        (BATTERIES, 'BATTERIES'),
        (PORT_BAG, 'PORTE-BAGAGES ARRIÈRE'),
        (GAL_TOIT_COFFRES, 'CALERIES DE TOIT ET COFFRES'),
        (ATT_REMORQUE, 'ATTELAGES POUR REMORQUE'),
        (PNEUS_JANTES, 'PNEUS ET JANTES'),
        (ATT_REMORQUE, 'ATTELAGES POUR REMORQUE'),
        (ACCESS_PNEUS, 'ACCESSOIRES PNEUS ET JANTES'),
        (OUTILS, 'OUTILS'),
        (ENTRE_PNEUS, 'ENTRETIEN DES PNEUS'),
        (ENTRE_JANTES, 'ENTRETIEN DES JANTES'),
        (ENTRE_INTER, 'ENTRETIEN INTERIEUR'),
        (ENTRE_MOTEUR, 'ENTRETIEN MOTEUR'),
        (VOLANTS, 'VOLANTS ET MOYEUX DE VOLANTS'),
        (ASSIST_PANNE, 'ASSISTANCE PANNE'),
        (EPON_CHIF_BROS, 'EPONGES, CHIFFON, BROSSES')
    ]

    categorie_name = models.CharField(max_length=200, choices=CATEGORIES)
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

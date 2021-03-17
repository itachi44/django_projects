from django.contrib import admin
from .models import MarqueVoiture, Annee, ModeleVoiture, CategoriePiece, PieceVoiture, LigneCommande, Client, \
    CompteClient



#####################################   affichage indépendamment des relations   #################################


#############################################   relation OneToOne    #############################################


#############################################  relation ManyToMany   ##################################################



class MarqueVoitureAdmin(admin.ModelAdmin):
    list_display = ('marques',)
    search_fileds = ('marques',)


class AnneeAdmin(admin.ModelAdmin):
    list_display = ('annee',)
    search_fields = ('annee',)


class ModelVoitureAdmin(admin.ModelAdmin):
    list_display = ('modele_label', 'annee',)
    list_filter = ('modele_label', 'annee', 'marque',)
    search_fields = ('modele_label', 'annee', 'marque')


class CategoriePieceAdmin(admin.ModelAdmin):
    list_display = ('categorie_name',)
    search_fields = ('catégorie_name',)


class PieceVoitureAdmin(admin.ModelAdmin):
    list_display = ('label_piece', 'prix_piece', 'desc_piece',)
    list_filter = ('label_piece',)
    search_fields = ('label_piece', 'desc_piece')


"""
class LigneCommandeAdmin(admin.ModelAdmin):
    list_display = ('Pièces', 'Prix', 'Quantité', 'montantLigne')
    list_filter = ('Pièces',)
    search_fields = 'Pièces'
    def montantLigne(self, LigneCommande):
        return LigneCommande.prix_piece * LigneCommande.qte
    montantLigne.short_description = 'Motant total' 
"""


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom_client', 'prenom_client', 'tel_client')
    list_filter = ('nom_client', 'prenom_client', 'tel_client',)
    search_fields = ('nom_client', 'prenom_client', 'tel_client')


class CompteClientAdmin(admin.ModelAdmin):
    list_display = ('email_client', 'mdp_client',)


admin.site.register(MarqueVoiture, MarqueVoitureAdmin)
admin.site.register(Annee, AnneeAdmin)
admin.site.register(ModeleVoiture, ModelVoitureAdmin)
admin.site.register(CategoriePiece, CategoriePieceAdmin)
admin.site.register(PieceVoiture, PieceVoitureAdmin)
# admin.site.register(LigneCommande, LigneCommandeAdmin)
admin.site.register(Client, ClientAdmin)
# admin.site.register(Commande)
admin.site.register(CompteClient, CompteClientAdmin)
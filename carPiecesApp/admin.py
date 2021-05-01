from django.contrib import admin
from .models import MarqueVoiture, ModeleVoiture, CategoriePiece, PieceVoiture, LigneCommande, Client, \
    CompteClient, Commande, Motorisation


class MarqueVoitureAdmin(admin.ModelAdmin):
    list_display = ('marques',)
    search_fileds = ('marques',)


class ModelVoitureAdmin(admin.ModelAdmin):
    list_display = ('modele_label', 'annee',)
    list_filter = ('modele_label', 'annee', 'marque',)
    search_fields = ('modele_label', 'annee', 'marque')


class MotorisationAdmin(admin.ModelAdmin):
    list_display = ('motorisation', 'modele_label')
    list_filter = ('motorisation', )
    search_fields = ('motorisation', )


class CategoriePieceAdmin(admin.ModelAdmin):
    list_display = ('categorie_name',)
    search_fields = ('catégorie_name',)


class PieceVoitureAdmin(admin.ModelAdmin):
    list_display = ('label_piece', 'prix_piece', 'desc_piece',)
    list_filter = ('label_piece',)
    search_fields = ('label_piece', 'desc_piece')


class LigneCommandeAdmin(admin.ModelAdmin):
    list_display = ('pieceVoiture', 'prix_piece', 'qte', 'montantLigne')
    list_filter = ('pieceVoiture',)
    search_fields = ('pieceVoiture',)

    def montantLigne(self, ligne_commande):
        return ligne_commande.prix_piece * ligne_commande.qte

    montantLigne.short_description = 'Motant total'


class CommandeAdmin(admin.ModelAdmin):
    list_display = ('date_commande', 'montant_total',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom_client', 'prenom_client', 'tel_client')
    list_filter = ('nom_client', 'prenom_client', 'tel_client',)
    search_fields = ('nom_client', 'prenom_client', 'tel_client')


class CompteClientAdmin(admin.ModelAdmin):
    list_display = ('email_client', 'mdp_client',)


admin.site.register(MarqueVoiture, MarqueVoitureAdmin)
admin.site.register(ModeleVoiture, ModelVoitureAdmin)
admin.site.register(Motorisation, MotorisationAdmin)
admin.site.register(CategoriePiece, CategoriePieceAdmin)
admin.site.register(PieceVoiture, PieceVoitureAdmin)
admin.site.register(LigneCommande, LigneCommandeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(CompteClient, CompteClientAdmin)

from rest_framework import serializers
from carPiecesApp.models import MarqueVoiture, Annee, ModeleVoiture, CategoriePiece,PieceVoiture,LigneCommande, Client, Commande, CompteClient

class NoteSerializer(serializers.ModelSerializer):
    marque = serializers.CharField(max_length=180, allow_blank=False)
    class Meta:
        model = MarqueVoiture
        fields = ['marque']
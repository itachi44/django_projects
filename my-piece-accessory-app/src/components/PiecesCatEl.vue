<template>
	<div>
		<b-row>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="ENTRAINEMENT/TRANSMISSION" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/entr_trans.jpeg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Éléments de transmission</div>
				<div>Courroies trapézoïdales</div>
				<div>Arbres de transmission</div>
				<div>Embrayages</div>
				<div>Joints de transmission</div>
				<div>Roulements</div>
			</b-col>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="FREINS" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/freins.jpeg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Etriers</div>
				<div>Plaquettes</div>
				<div>Assistance au freinage</div>
				<div>Rotors de disque</div>
				<div>Druites</div>
				<div>Calibres</div>
				<div>Tambours</div>
				<div>Maitres-cylindres</div>
			</b-col>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="AMÉNAGEMENTS INTERIEURS" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/entre_inte.jpg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Accoudoirs</div>
				<div>Installation climatisation</div>
			</b-col>
		</b-row>
		<hr/>
		<b-row>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="MOTEURS/PIECES DE MOTEURS" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/moteurs.jpeg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div><router-link to="piecesdetachees/testroute">Démarreurs</router-link></div>
				<div>Chip-tuning</div>
				<div>Alimentation carburant</div>
				<div>Refroidissements moteur</div>
				<div>Alternateurs</div>
				<div>Compartiments moteur</div>
				<div>Carters d'huile</div>
				<div>Courroies de distribution</div>
				<div>Culasses de cylindre</div>
			</b-col>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="ESSUIE-GLACES/LAVE-GLACES" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/essuie-glace.jpeg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Balais d'essuie-glaces</div>
				<div>Moteurs d'essuie-glaces</div>
			</b-col>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="CAPTEURS" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/capteurs.jpeg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Capteurs de freins</div>
				<div>Capteurs de vitesse</div>
				<div>Contacteurs</div>
			</b-col>
		</b-row>
		<hr/>
		<b-row>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="ALLUMAGE" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/allumage.jpeg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Bougies de préchauffage</div>
				<div>Système d'allumage et chauffage</div>
				<div>Bougies d'allumage</div>
				<div>Câbles d'allumage</div>
			</b-col>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="SYSTEME D'ECHAPPEMENT" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/syst_echap.png" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Systèmes d'échappement</div>
				<div>Joints</div>
				<div>Capteurs d'oxygène</div>
				<div>Pièces d'assemblage</div>
			</b-col>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="DIRECTION ET SUSPENSION" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/direction_suspension.jpeg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Châssis complets</div>
				<div>Ressorts d'appui de coupelle</div>
				<div>Bras de suspension</div>
				<div>Suspension roues</div>
				<div>Embouts biellette de direction</div>
				<div>Barres stabilisatrices</div>
				<div>Amortisseurs</div>
				<div>Ressorts de raccord bas</div>
			</b-col>
		</b-row>
		<hr/>
		<b-row>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="BATTERIES" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/batteries.jpeg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Batteries</div>
			</b-col>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="PHARES ET INCUBATEURS" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/phares_incubateurs.jpg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Indicateurs</div>
				<div>Lampes à filament</div>
				<div>feux arrière</div>
				<div>Éclairage intérieur</div>
				<div>Alternateurs</div>
				<div>Relais</div>
				<div>Phares</div>
				<div>Feux de position</div>
			</b-col>
			<b-col class="colm" md="4">
				<label>
					<b-col>
						<b-dropdown class="dropcat1" text="PERSONNALISATION" variant="#" block menu-class="w-100">
							<b-dropdown-item class="dropitem" href="#"><img src="../../../../PiecesImages/resize/person.jpeg" alt=""></b-dropdown-item>
						</b-dropdown>
					</b-col>
				</label>
				<div>Garde-boue</div>
				<div>Capots pour moteur</div>
				<div>Coques pour rétroviseur</div>
			</b-col>
		</b-row>
		<hr />
		<div>
			<router-view />
		</div>
	</div>
</template>

<script>
export default {
	name: 'PiecesCatEl'
}
</script>

<style lang="scss" scoped>
	label{
		background: #F18E33;
		border: 2px solid #9D1989;
		width: 300px;
		padding: 2px;
		margin-top: 5px;
		font-size: 15px;

	}
	label~div{
		width: 260px;
		margin-left: 70px;
		text-align: left;
		padding: 3px;
	}
	hr{
		border: 1px solid #9D1989;
	}
	.images{
		text-align: center;
	}
</style>
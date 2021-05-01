<template>
	<div>
    <h6 :style="{'text-align': 'center'}"> 🚘 Résultats pour la recherche effectuée</h6>
    <hr/>
      <div>
        <b-row align-v='center' align-h='center'>
          <b-col md="3" class="ab">
            <span>Trouvez la catégorie</span>
          </b-col>
          <b-col md="6" class="cd">
            <b-form-input v-model="text" placeholder="Veuillez saisir dans ce champ!" :style="{'font-size': '13px'}"></b-form-input>
          </b-col>
          <b-col md="3" class="ef">
            <b-button :style="{'background-color': '#F18E33', 'color':'#000000','font-size': '13px', 'margin-top': '1px'} "><b-icon icon="search"></b-icon> Rechercher</b-button>
          </b-col>
        </b-row>
      </div>
      <hr/>
  </div>
</template>

<script>
export default {
	name: 'SearchBar'
}
</script>

<style lang="scss" scoped>
  hr{
		border: 1px solid #9D1989;
	}
	.ab, .cd, .ef{
		text-align: center;
	}
</style>
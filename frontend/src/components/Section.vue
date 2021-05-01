<template>
   <b-container class="container1 m-0 p-0" fluid>
 <div class="img">
  <img class="image"  width="100%" src="../assets/bg.jpg">
  
    <b-card-text class="TextOverlay">
            NOUS VOUS AIDONS A TROUVER LA <span style="color:#9D1989">PIECE DE VOTRE</span> <span style="color:#9D1989" >CHOIX</span> ET ADAPTEE A VOS BESOINS.
   </b-card-text>
   <div class="formHome">
   <FormHome/>
</div>


</div>
<hr style="background-color:#000; width:90%"/>
<h4>Top marques de voitures</h4>
</b-container>
</template>

<script>

import FormHome from '@/components/FormHome.vue'
export default {
  name: 'Section',
  components: {
    FormHome
  }
}

</script>

<style scoped>
@media screen and (min-width: 1024px)
{
.img{
    display: flex;
    margin: 0! important
}
.image{
  margin: 0 !important
  
}

.container1{
  margin-bottom: 3% !important;
  padding-bottom: 0!important
 
}

.TextOverlay{
  position: absolute;
  top: 20%;
  right: 50%;
  background-color: transparent;
  max-width: 500px;
  color: #272f89;
  font-size: 1.6em;
  font-weight: bold;
  z-index: 0;
  opacity: 1;
}

.formHome{
  position: absolute;
  top:10%;
  right: 15%;
  background-color: #9D1989;
  width: 30%;

}
}
@media screen and (max-width: 1024px)
{
.formHome{
  background-color: #9D1989;
}

.TextOverlay{
  font-size: 1.2em;
}
}
</style>
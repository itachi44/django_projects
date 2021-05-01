<template>
<div class="form">
  <form >
    <h4 style="text-align:left; color:#fff; padding-top:5%; padding-left:7%; padding-bottom:0;">Definissez la voiture</h4>
    <hr style="background-color:#fff; width:85%">
     <select class=" select browser-default custom-select custom-select-lg mb-3">
      <option selected>Choisir une année</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </select>
    <br/>
 <select class=" select browser-default custom-select custom-select-lg mb-3">
      <option selected>Choisir une marque</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </select>  
    <br/>
    <select class=" select browser-default custom-select custom-select-lg mb-3">
      <option selected>Choisir un modèle</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </select>
    <br/>
     <select class=" select browser-default custom-select custom-select-lg mb-3">
      <option selected>Choisir une matriculation</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </select>
    <div class="text-center mt-4">
      <button style="color:#fff; height:3em; font-size:1.2em;" class="btn btn-unique" type="submit"><b-icon style="transform:scale(0.9);" icon="search"></b-icon> Rechercher</button>
    </div>
  </form>
  </div>
</template>


<script>
export default {
  name: 'Section',
}

</script>

<style scoped>
.select{
  width: 90%;
}
.btn-unique{
  background-color: #F18E33;
  margin-bottom: 5%;
  transition: all 0.5s ease-out;
}
.btn-unique:hover{
  box-shadow: 2px 2px 2px #6e6f6c;
}
.btn-unique:active{
  transform: scale(0.9);
  border: none;
}
.form{
  box-shadow: 2px 2px 2px #262f42;
}

</style>
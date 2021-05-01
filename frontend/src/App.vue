<template>
  <div id="app">
    <b-container fluid tag="main" id="app" v-cloak>
    <Home/>

    </b-container>
    <router-view/>
  </div>
</template>

<script>

export default {
  name:'App',
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.dropdown .nav-link{
  text-decoration: none;
  color: #000;
}



</style>

<template>
  <div id="app">
    <div id="nav">
      <router-link to="/piecesdetachees">Pièces détachées</router-link> |
      <router-link to="/accessoires">Accessoires</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  font-size: 12px;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #9D1989;
    }
  }
}
</style>

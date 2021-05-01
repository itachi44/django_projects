<template>
  <div>
    <search-bar />
    <accessoires-cat-el/>
  </div>
</template>

<script>
import AccessoiresCatEl from './AccessoiresCatEl.vue'
import SearchBar from './SearchBar.vue'
export default {
	name: 'PiecesComp',
  components: {
    SearchBar,
    AccessoiresCatEl
  }
}
</script>

<style lang="scss" scoped>
	
</style>

<template>
  <div>
    <search-bar />
    <pieces-cat-el/>
  </div>
</template>

<script>
import PiecesCatEl from './PiecesCatEl.vue'
import SearchBar from './SearchBar.vue'
export default {
	name: 'PiecesComp',
  components: {
    SearchBar,
    PiecesCatEl
  }
}
</script>

<style lang="scss" scoped>
	
</style>

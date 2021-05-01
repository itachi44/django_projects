<template>
   <b-container class=" m-0 p-0" fluid>
       <Carousel1/>
       <Carousel2/>
</b-container>
</template>

<script>

import Carousel1 from '@/components/Carousel1.vue'
import Carousel2 from '@/components/Carousel2.vue'
export default {
  name: 'SectionBottom',
  components: {
    Carousel1,
    Carousel2
  }
}

</script>

<style scoped>


</style>
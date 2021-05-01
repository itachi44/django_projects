<template>
 <div class="home">
    <Header/>
    <Section/>
    <SectionBottom/>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import Section from '@/components/Section.vue'
import Footer from '@/components/Footer.vue'
import SectionBottom from '@/components/SectionBottom.vue'

export default {
  name:'Home',
  components: {
   Header,
  Footer,
  Section,
  SectionBottom,
  }
}
</script>

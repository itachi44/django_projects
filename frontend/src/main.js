import Vue from 'vue'
import App from './App.vue'
import router from './router'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import {MdButton, MdContent, MdTabs} from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css' 
import 'vue-material/dist/theme/default.css'


Vue.config.productionTip = false
Vue.use(MdButton)
Vue.use(MdContent)
Vue.use(MdTabs)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import store from './store'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

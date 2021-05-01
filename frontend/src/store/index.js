import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    categorie:{
      labels:[{label:"elt1"},{label:"elt2"},{label:"elt3"},{label:"elt4"},{label:"elt5"},{label:"elt6"},{label:"elt7"},{label:"elt8"}]
    },
      labelsArticles:{
        slide1:[{label:"amortisseur",img:'amortisseur.jpg'},{label:"essui",img:'essui.jpg'},{label:"truc1",img:'truc1.jpg'}],
        slide2:[{label:"truc2",img:'truc2.jpg'},{label:"truc3",img:'truc3.jpg'},{label:"truc3", img:'truc3.jpg'}],
        slide3:[{label:"truc4",img:'truc4.jpg'},{label:"truc5",img:'truc5.jpg'},{label:"truc6",img:'truc6.jpg'}],
        slide4:[{label:"truc7", img:'truc7.jpg'}]
        },
  
      labelsMarques:{
        slide1:[{label:"bmw",img:'bmw.jpg'},{label:"citroen",img:'citroen.jpg'},{label:"peugeot",img:'peugeot.jpg'},{label:"renault",img:'renault.jpg'}]
      }


  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})

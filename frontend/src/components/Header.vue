<template>
  <b-navbar toggleable="md"
              class=" py-0 my-0"
              type="light"
              variant="white">
      <b-nav-toggle target="nav_collapse"></b-nav-toggle>
      <b-navbar-brand class="p-0" href="#"><img class="logo"  width="100%" src="../assets/Logo_titre.png"></b-navbar-brand>
      <b-collapse is-nav
                  id="nav_collapse">
        <b-navbar-nav class="menu"> 
          <div @mouseover="onOver" @mouseleave="onLeave">
      <b-nav-item-dropdown  ref="dropdown" class="categorie item"  text="Categorie" right>
        <b-dropdown-item  id="more" >Pièces détachées <b-icon style="color:#000;"  class="icon" icon="arrow-bar-right"></b-icon> 
        <div class="subdropdown">
          <ul v-for="elt in $store.state.categorie.labels" :key="elt.label">
            <li> <b-link href="#">  <span class="categorieElt" style="color:black;"> {{elt.label}}</span> </b-link></li> 
          </ul>
        </div>
        </b-dropdown-item>
               <b-dropdown-divider></b-dropdown-divider>
    <b-dropdown-item id="more" style="text-align:center;" >Accessoires <b-icon  style="color:#000;" icon="arrow-bar-right"></b-icon>
      <div class="subdropdown">
          <ul v-for="elt in $store.state.categorie.labels" :key="elt.label">
            <li> <b-link href="#">  <span class="categorieElt" style="color:black;"> {{elt.label}}</span> </b-link></li>
        
          </ul>
        </div>
    </b-dropdown-item>
      </b-nav-item-dropdown> 
      
      
      </div>
          <b-nav-item  class="conditionVente item" href="#"> <span>Condition de vente</span></b-nav-item>
          <b-nav-item class="navItem1 item" toggle-class="text-dark" href="#" ><b-icon  class="iconSignin" icon="box-arrow-right"></b-icon> <span> se connecter</span> </b-nav-item>
          <b-nav-item class="navItem2 item " href="#"> <span>s'inscrire</span> <b-icon class="iconSignin" icon="person-fill"></b-icon></b-nav-item>
          <b-nav-item class="navItem3 item" href="#"><span>votre panier</span> <b-icon class="iconBag" icon="bag-check"></b-icon></b-nav-item>    
        </b-navbar-nav>
        
      </b-collapse>
    </b-navbar>
</template>

<script>
export default {
  name: 'Header',
  methods: {
      onOver() {
        this.$refs.dropdown.visible = true;
      },
      onLeave() {
        this.$refs.dropdown.visible = false;
      },
      modulo(index){
        return index%4!=0
      }
    }
}

</script>

<style>

@media screen and (min-width: 1024px)
{

.navbar-nav *:hover{
  text-decoration-line: none !important

}

.subdropdown{
  display: none;
  background-color: #fff;
  position: absolute;
  left: 97%;
  top: 9%;
}
.subdropdown{
  display: none;
}
.subdropdown ul{
    list-style-type: none;
}
.subdropdown ul{

  
}
#more:hover .subdropdown{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
}
#more{
  color:#9D1989; 
  font-weight: bold;
  text-decoration: none;
}
#more:hover{
  transform: scale(1.05);
}
.conditionVente{
  margin-left: 5%;
  transition: all 0.2s ease-out;
}

.iconSignin{
  margin-bottom: 1%;
  color: black;
}
.iconBag{
  margin-bottom: 2%;
  color: black;
}
.nav-item:nth-child(n):not(:first-child) *{
  text-decoration: none;
}
.nav-item:hover:not(.categorie){
  transform: scale(1.1);
  text-decoration: none;
}
.nav-item:nth-child(n):not(:first-child):active{
  transform: scale(0.9);
}
.nav-item:nth-child(n+3) {
  border-radius: 5px;
  text-decoration: none;
}

.nav-item:nth-child(n+3) {
transition: all 0.5s ease-out;
}
.nav-item:nth-child(n+3):hover {
  background-color:#9D1989;
  opacity: 0.8;
}

.nav-item:nth-child(n+3):hover span{
  color: #fff;
}
.nav-item:nth-child(n+3):hover .b-icon{
  color: #fff;
  text-decoration: none;
}
.navItem1{
  margin-left:10% ;
}
span{
  color: black;
  font-size: 1.2em;
}
.navItem2, .navItem3{
  margin-left:3% ;
}
.menu{
  width: 100%;
  margin-top: 5%;
}
}
.mb-3{
  padding-bottom: 0;

}
.dropdown{
  text-align: center;
}


.categorie, .conditionVente{
  border-bottom:5px solid #9D1989;

}
.navbar-brand {
  width: 20%;
  display: flex;
  transform: scale(0.9);
}


@media screen and (max-width: 1024px)
{
  .navbar-brand {
  width: 28%;
  display: flex;
  transform: scale(1);
}
}

</style>
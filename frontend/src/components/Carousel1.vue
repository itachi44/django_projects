<template>
  <div class="carousel1" >
    <b-carousel
      id="carousel-1"
      v-model="slide"
      controls
      indicators
      :interval="4000"
      background="#fff"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >

<b-carousel-slide  style="height:280px;">

  <b-container fluid class="p-4 bg-white">
  <b-row v-if="largeur>=1024">
      <b-col v-for="elt in $store.state.labelsMarques.slide1" :key="elt.img">
        <div class="hovereffect">
            <b-img class="imgItem img-responsive" thumbnail fluid v-bind:src="require('../assets/marques/' + elt.img)" alt="Image 1"></b-img>
            <div class="overlay">
               <a href="#"> <h2  >Visiter</h2></a>
                
            </div>
         </div>

      </b-col>
    </b-row>

      <!--rendu mobile-->
    <b-row v-else>

      <b-col >
        <div class="hovereffect">
            <b-img class="imgItem img-responsive" fluid-grow v-bind:src="require('../assets/marques/' + $store.state.labelsMarques.slide1[0].img)" alt="Image 1"></b-img>
            <div class="overlay">
               <a href="#"> <h2  >Visiter</h2></a>
                
            </div>
         </div>
      </b-col>
    </b-row>

  </b-container>   
</b-carousel-slide> 

      <b-carousel-slide  style="height:280px;">

  <b-container fluid class="p-4 bg-white">
  <b-row v-if="largeur>=1024">
      <b-col v-for="elt in $store.state.labelsMarques.slide2" :key="elt.img">
        <div class="hovereffect">
            <b-img class="imgItem img-responsive" thumbnail fluid v-bind:src="require('../assets/marques/' + elt.img)" alt="Image 1"></b-img>
            <div class="overlay">
               <a href="#"> <h2  >Visiter</h2></a>
                
            </div>
         </div>

      </b-col>
    </b-row>

      <!--rendu mobile-->
    <b-row v-else>

      <b-col >
        <div class="hovereffect">
            <b-img class="imgItem img-responsive" fluid-grow v-bind:src="require('../assets/marques/' + $store.state.labelsMarques.slide1[1].img)" alt="Image 1"></b-img>
            <div class="overlay">
               <a href="#"> <h2  >Visiter</h2></a>
                
            </div>
         </div>
      </b-col>
    </b-row>

  </b-container>   
</b-carousel-slide> 

<b-carousel-slide  style="height:280px;">

  <b-container fluid class="p-4 bg-white">
  <b-row v-if="largeur>=1024">
      <b-col v-for="elt in $store.state.labelsMarques.slide3" :key="elt.img">
        <div class="hovereffect">
            <b-img class="imgItem img-responsive" thumbnail fluid v-bind:src="require('../assets/marques/' + elt.img)" alt="Image 1"></b-img>
            <div class="overlay">
               <a href="#"> <h2  >Visiter</h2></a>
                
            </div>
         </div>

      </b-col>
    </b-row>

      <!--rendu mobile-->
    <b-row v-else>

      <b-col >
        <div class="hovereffect">
            <b-img class="imgItem img-responsive" fluid-grow v-bind:src="require('../assets/marques/' + $store.state.labelsMarques.slide1[3].img)" alt="Image 1"></b-img>
            <div class="overlay">
               <a href="#"> <h2  >Visiter</h2></a>
                
            </div>
         </div>
      </b-col>
    </b-row>

  </b-container>   
</b-carousel-slide> 

    </b-carousel>

    <hr style="background-color:#000; width:90%"/>
<h4>Top pièces les plus vendues</h4>
  </div>
</template>

<script>
  export default {
      name:"Carousel1",
    data() {
      return {
        slide: 0,
        sliding: null,
        largeur:0
      }
    },
    methods: {
      onSlideStart() {
        this.sliding = true
      },
      onSlideEnd() {
        this.sliding = false
      },
      getWidth: function(){
        var v =this;
        setInterval(function(){
          v.largeur=window.innerWidth;
        }, 100)
      }
    },
     beforeMount(){
      this.getWidth()
    }
   
  }

  </script>

  <style scoped>


.carousel1{
      margin:0;
  }

.imgItem{
    transform: scale(1.1);
    height: 170px;
    width: 100%;
}


/*hover overlay effect */

.hovereffect {
    width: 100%;
    height: 100%;
   /* float: left;*/
    overflow: hidden;
   /* position: relative;*/
    text-align: center;
    cursor: default;
}
.hovereffect .overlay {
    width: 100%;
    position: absolute;
    overflow: hidden;
    left: 0;
	top: auto;
	bottom: 0;
	padding: 1em;
	height: 4.75em;
	-webkit-transition: -webkit-transform 0.35s;
	transition: transform 0.35s;
	-webkit-transform: translate3d(0,100%,0);
	transform: translate3d(0,100%,0);
	visibility: hidden;

}

.hovereffect img {
    display: block;
    position: relative;
	-webkit-transition: -webkit-transform 0.35s;
	transition: transform 0.35s;
}

.hovereffect:hover img {
-webkit-transform: translate3d(0,-10%,0);
	transform: translate3d(0,-10%,0);
}

.hovereffect h2 {
    text-transform: uppercase;
    color: #fff;
    text-align: center;
    position: relative;
    font-size: 17px;
    padding: 10px;
    background: rgba(0, 0, 0, 0.6);
	float: left;
	margin: 0px;
	display: inline-block;
}

.hovereffect a.info {
    display: inline-block;
    text-decoration: none;
    padding: 7px 14px;
    text-transform: uppercase;
	color: #fff;
	border: 1px solid #fff;
	margin: 50px 0 0 0;
	background-color: transparent;
}
.hovereffect a.info:hover {
    box-shadow: 0 0 5px #fff;
}


.hovereffect h2 {
	-webkit-transition: -webkit-transform 0.35s;
	transition: transform 0.35s;
	-webkit-transform: translate3d(0,200%,0);
	transform: translate3d(0,200%,0);
	visibility: visible;
}



.hovereffect:hover .overlay,
.hovereffect:hover h2{
	-webkit-transform: translate3d(0,0,0);
    transform: translate3d(0,0,0);
    background-color: #9D1989;
}

.hovereffect:hover h2 {
	-webkit-transition-delay: 0.05s;
    transition-delay: 0.05s;
}

@media screen and (max-width: 1024px)
{

}

@media screen and (min-width: 1024px)
{

}





  </style>
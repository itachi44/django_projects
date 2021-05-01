<template>
  <div class="carousel1" >
    <b-carousel
      id="carousel-1"
      v-model="slide"
      controls
      indicators
      :interval="6000"
      background="#fff"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >

      <b-carousel-slide  style="height:280px;">

      <b-container  fluid class="cont p-4 bg-white">
  <b-row  v-if="largeur>=1024">
    <b-col  v-for="elt in $store.state.labelsArticles.slide1" :key="elt.img">

      <div class="hovereffect">
      <b-img class="articleItem img-responsive" thumbnail fluid v-bind:src="require('../assets/articles/' + elt.img)" alt="Image 1"></b-img>
        <div class="overlay">
           <h2>{{elt.label}}</h2>
           <a class="info" href="#">Acheter</a>
        </div>
    </div>


    </b-col>
  </b-row>


      <!--rendu mobile-->
    <b-row v-else>

     <b-col>

      <div class="hovereffect">
      <b-img class="articleItem img-responsive" thumbnail fluid v-bind:src="require('../assets/articles/' + $store.state.labelsArticles.slide1[0].img)" alt="Image 1"></b-img>
        <div class="overlay">
           <h2>{{$store.state.labelsArticles.slide1[0].label}}</h2>
           <a class="info" href="#">Acheter</a>
        </div>
    </div>


    </b-col>
    </b-row>
</b-container>  
      </b-carousel-slide> 


       <b-carousel-slide  style="height:280px;">

      <b-container  fluid class="cont p-4 bg-white">
  <b-row  v-if="largeur>=1024">
    <b-col  v-for="elt in $store.state.labelsArticles.slide2" :key="elt.img">

      <div class="hovereffect">
      <b-img class="articleItem img-responsive" thumbnail fluid v-bind:src="require('../assets/articles/' + elt.img)" alt="Image 1"></b-img>
        <div class="overlay">
           <h2>{{elt.label}}</h2>
           <a class="info" href="#">Acheter</a>
        </div>
    </div>


    </b-col>
  </b-row>


      <!--rendu mobile-->
    <b-row v-else>

     <b-col>

      <div class="hovereffect">
      <b-img class="articleItem img-responsive" thumbnail fluid v-bind:src="require('../assets/articles/' + $store.state.labelsArticles.slide2[0].img)" alt="Image 1"></b-img>
        <div class="overlay">
           <h2>{{$store.state.labelsArticles.slide2[0].label}}</h2>
           <a class="info" href="#">Acheter</a>
        </div>
    </div>


    </b-col>
    </b-row>
</b-container>  
      </b-carousel-slide> 


       <b-carousel-slide  style="height:280px;">

      <b-container  fluid class="cont p-4 bg-white">
  <b-row  v-if="largeur>=1024">
    <b-col  v-for="elt in $store.state.labelsArticles.slide3" :key="elt.img">

      <div class="hovereffect">
      <b-img class="articleItem img-responsive" thumbnail fluid v-bind:src="require('../assets/articles/' + elt.img)" alt="Image 1"></b-img>
        <div class="overlay">
           <h2>{{elt.label}}</h2>
           <a class="info" href="#">Acheter</a>
        </div>
    </div>


    </b-col>
  </b-row>


      <!--rendu mobile-->
    <b-row v-else>

     <b-col>

      <div class="hovereffect">
      <b-img class="articleItem img-responsive" thumbnail fluid v-bind:src="require('../assets/articles/' + $store.state.labelsArticles.slide3[0].img)" alt="Image 1"></b-img>
        <div class="overlay">
           <h2>{{$store.state.labelsArticles.slide3[0].label}}</h2>
           <a class="info" href="#">Acheter</a>
        </div>
    </div>


    </b-col>
    </b-row>
</b-container>  
      </b-carousel-slide> 


       <b-carousel-slide  style="height:280px;">

      <b-container  fluid class="cont p-4 bg-white">
  <b-row  v-if="largeur>=1024">
    <b-col  v-for="elt in $store.state.labelsArticles.slide4" :key="elt.img">

      <div class="hovereffect">
      <b-img class="articleItem img-responsive" thumbnail fluid v-bind:src="require('../assets/articles/' + elt.img)" alt="Image 1"></b-img>
        <div class="overlay">
           <h2>{{elt.label}}</h2>
           <a class="info" href="#">Acheter</a>
        </div>
    </div>


    </b-col>
  </b-row>


      <!--rendu mobile-->
    <b-row v-else>

     <b-col  v-for="elt in $store.state.labelsArticles.slide4" :key="elt.img">

      <div class="hovereffect">
      <b-img class="articleItem img-responsive" thumbnail fluid v-bind:src="require('../assets/articles/' + $store.state.labelsArticles.slide4[0].img)" alt="Image 1"></b-img>
        <div class="overlay">
           <h2>{{$store.state.labelsArticles.slide4[0].label}}</h2>
           <a class="info" href="#">Acheter</a>
        </div>
    </div>


    </b-col>
    </b-row>
</b-container>  
      </b-carousel-slide> 
    </b-carousel>

  </div>
</template>

<script>
  export default {
      name:"Carousel2",
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

.articleItem{
    transform: scale(1.1);
    height: 170px;
    width: 90%;
}



.hovereffect {
width:100%;
height:100%;
float:left;
overflow:hidden;
position:relative;
text-align:center;
cursor:default;
}

.hovereffect .overlay {
width:100%;
height:100%;
position:absolute;
overflow:hidden;
top:0;
left:0;
opacity:0;
background-color:rgba(0,0,0,0.5);
-webkit-transition:all .4s ease-in-out;
transition:all .4s ease-in-out
}

.hovereffect img {
display:block;
position:relative;
-webkit-transition:all .4s linear;
transition:all .4s linear;
}

.hovereffect h2 {
text-transform:uppercase;
color:#fff;
text-align:center;
position:relative;
font-size:17px;
background:rgba(0,0,0,0.6);
-webkit-transform:translatey(-100px);
-ms-transform:translatey(-100px);
transform:translatey(-100px);
-webkit-transition:all .2s ease-in-out;
transition:all .2s ease-in-out;
padding:10px;
}

.hovereffect a.info {
text-decoration:none;
display:inline-block;
text-transform:uppercase;
color:#fff;
border:1px solid #fff;
background-color:transparent;
opacity:0;
filter:alpha(opacity=0);
-webkit-transition:all .2s ease-in-out;
transition:all .2s ease-in-out;
margin:50px 0 0;
padding:7px 14px;
}

.hovereffect a.info:hover {
box-shadow:0 0 3px #fff;
}

.hovereffect:hover img {
-ms-transform:scale(1.2);
-webkit-transform:scale(1.2);
transform:scale(1.2);
}

.hovereffect:hover .overlay {
opacity:1;
filter:alpha(opacity=100);
}

.hovereffect:hover h2,.hovereffect:hover a.info {
opacity:1;
filter:alpha(opacity=100);
-ms-transform:translatey(0);
-webkit-transform:translatey(0);
transform:translatey(0);
}

.hovereffect:hover a.info {
-webkit-transition-delay:.2s;
transition-delay:.2s;
}


@media screen and (max-width: 1024px)
{

}

@media screen and (min-width: 1024px)
{

}


  </style>

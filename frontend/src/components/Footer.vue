<template>
<b-container class="footer my-0 px-3" fluid>
    <mdb-container class=" m-0 text-center text-md-left ">
      <mdb-row class="text-center text-md-left mt-2 pb-3 " style="margin-left:3%;">
        <mdb-col md="3" lg="3" xl="3" class="mx-auto mt-3" >
          <p><a style="color:#fff; text-decoration:none;" class="footerItem"  href="#">Nos partenaires</a></p>
          <p><a style="color:#fff; text-decoration:none;" class="footerItem" href="#">FAQ</a></p>
          <p><a style="color:#fff; text-decoration:none; " class="footerItem" href="#">Politique de confidentialité</a></p>
        </mdb-col>
        <hr class="w-100 clearfix d-md-none" />
        <mdb-col md="3" lg="3" xl="3"  class="mx-auto mt-3 ml-0">
          <p><a style="color:#fff; text-decoration:none;" class="footerItem" href="#">A propos de nous</a></p>
          <p><a style="color:#fff; text-decoration:none;"  class="footerItem" href="#">Nous contacter</a></p>
        </mdb-col>
       
        <hr class="w-100 clearfix d-md-none" />
        <mdb-col md="3" lg="3" xl="3" class="mx-auto mt-4" >
          <b-navbar-brand class="p-0 brand"  href="#"><img class="logo"  width="100%" src="../assets/Logo.png"></b-navbar-brand>
        </mdb-col>
        <hr class="w-100 clearfix d-md-none" />
       
      </mdb-row>
      <hr style="background-color:#fff; margin-left:4%" />
      <mdb-row class="d-flex align-items-center">
        <mdb-col md="8" lg="8">
          <p class="text-center mx-5 text-md-left grey-text" style="font-size:1.2em;">&copy; 2021 Total Business. Tous droits réservés </p>
        </mdb-col>
        <mdb-col md="4" lg="4" class="ml-lg-0">
          <div class="text-center text-md-right">
            <ul class="list-unstyled list-inline">
              <li class="list-inline-item"><a class="btn-floating btn-sm rgba-white-slight mx-1 icnFB" href="#" ><b-icon id="facebook" class="icon" icon="facebook"></b-icon></a></li>
                            <li class="list-inline-item"><a class="btn-floating btn-sm rgba-white-slight mx-1 icnInsta" href="#"><b-icon id="instagram" class="icon" icon="instagram"></b-icon></a></li>

              <li class="list-inline-item"><a class="btn-floating btn-sm rgba-white-slight mx-1 icnTW" href="#"><b-icon id="twitter" class="icon" icon="twitter"></b-icon></a></li>
            </ul>
          </div>
        </mdb-col>
      </mdb-row>
    </mdb-container>
  </b-container>
</template>


<script>
  import { mdbContainer, mdbRow, mdbCol } from 'mdbvue';
  export default {
    name: 'Footer',
    components: {
      mdbContainer,
      mdbRow,
      mdbCol
    }
  }
</script>

<style scoped>

.footer{
    background-image:linear-gradient(#F18E33,#9D1989);

}


p{
    color: #fff;
}
.icon{
  color: #fff;
  transform: scale(1.3);
}

.footerItem {
  position: relative;
  display: inline-block;
  font-size: 1.3em;
  color: #fff;
  overflow: hidden;
  background: linear-gradient(to right, #9D1989, midnightblue 50%, #fff 50%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-size: 200% 100%;
  background-position: 100%;
  transition: background-position 275ms ease;
}
.footerItem:hover {
  background-position: 0 100%;
  transform: scale(1.1);
}

.icnFB:hover #facebook{
  color: #0984e3;
  transform: scale(1.7);

}
.icnFB:hover, .icnInsta:hover{
  background-color: #fff;
}
.icnFB,.icnInsta,.icnTW {
transition: all 0.3s ease-out;
}
#facebook,#instagram,#twitter{
  transition: all 0.3s ease-out;
}


.icnInsta:hover #instagram{
  background-color: #9D1989;
  transform: scale(1.7);

}

.icnTW:hover #twitter{
  color: #0984e3;
  transform: scale(1.7);

}


@media screen and (min-width: 1024px)
{
.navbar-brand {
  width: 100%;
  display: flex;
  transform: scale(0.9);
}
.brand{
  margin-left: 20%;
  transform: scale(1.2);
}

}
@media screen and (max-width: 1024px)
{

.navbar-brand {
  width: 50%;
  display: flex;
  transform: scale(0.9);
}
.brand{
  margin-left: 25%;
  transform: scale(1.2);
}
}

</style>
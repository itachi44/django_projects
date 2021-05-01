<template>
    <b-card-group class="container">

        <b-card :header= " product_name ">
           <b-row>
               <img width="100%" class="img" src="">
           </b-row>
               <b-card-text>
                        <b-button class="left_arrow" size="sm">
                            <b-icon icon="chevron-left">
                            </b-icon>
                        </b-button>
                        <b-button class="right_arrow" size="sm" >
                            <b-icon icon="chevron-right">
                            </b-icon>
                        </b-button>
               </b-card-text>
        </b-card>

        <b-card header="Description">
            <b-card-text class="col1">
                <small>
                    {{ description }}
                </small>
            </b-card-text>
        </b-card>
        <b-card header="Achat">
            <row class="container w-100 justify-content-center align-items-center">
            <h6>
                {{price}} CFA
            </h6>
            <small>
                le taux TV1 est 1.8% frais hors livraison
            </small>
            </row>
            <row class="container align-items-center">
                <b-form inline class="container w-100 justify-content-center align-items-center">
                    <b-button size="sm" class="align-self-center">
                        <b-icon icon="chevron-left">
                            </b-icon>
                    </b-button>
                    <b-form-input disabled size="sm" :value="nombre_article" style="text-align:center; width:50%;">
                    </b-form-input>
                    <b-button size="sm" >
                        <b-icon icon="chevron-right">
                            </b-icon>
                    </b-button>
                </b-form>
            </row>
            <row class="buttons align-items-center">
                <b-button size="sm">
                    <b-icon icon="cart-fill"></b-icon>
                    <small>
                        Commander
                    </small>
                </b-button>
                <b-button size="sm">
                    <b-icon icon="bag"></b-icon>
                    <small>
                        Ajouter au panier
                    </small>
                </b-button>
            </row>
        </b-card>
    </b-card-group>
</template>


<script>
export default {
    name : 'Results',
    props: {
        product_name: {
            type: String,
            default: "Cable d'allumage"
        },
        description:{
            type: String,
            default: ""
        },
        price:{
            type: Number,
            default: 1500
        },
        nombre_article:{
            type: Number,
            default: 1
        }
    },
    methods:{

    }
}
</script>
    
    
<style scoped>
.card-header{
    background-color: #F19E33;
    color: white;
    height: 40px;
    margin: 0%;
    padding: auto;
    font-size: 14px;
    font-weight: bold;
}
.buttons button{
    background-color: #9d1989;
    margin: 2%;
    border-block-color: #9d1989;
}

.col1{
    text-align: left;
}

.nombreArticle{
    align-items: center;
}

</style>
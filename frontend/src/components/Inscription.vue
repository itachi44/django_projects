<template>
  <div>
    <b-button v-b-modal.modal-inscription>Inscription</b-button>

    <b-modal
      id="modal-inscription" centered hide-footer
      ref="modal"
    >
        <b-row>
            <b-col cols="4" class="logo_place" style="display:flex; flex-direction: row; justify-content:center;">
                <b-navbar-brand class="m-0 p-0" style="justify-content:center"><img class="logo" width="100%" src="../assets/Logo_b.png" style="margin-top: 100%"></b-navbar-brand>
            </b-col>
            <b-col cols="8">
              <b-form>
                <b-form-row class="m-2">
                  <b-col name="icone" cols="2" class="h1">
                    <b-icon icon="person" style="color:#9d1989"></b-icon>
                  </b-col>
                  <b-col name="scripts">
                    <b-row>
                    <h6 class="m-0 p-0 ml-2"> Inscription</h6>
                    <small class="m-0 p-0 ml-2">
                        Vous êtes nouveau et vous souhaitez devenir membre? C'est ici
                    </small>
                    </b-row>
                 </b-col>
                </b-form-row>
                <b-form-row class="m-2">
                    <b-form-input v-model="prenom" type="text" name="prenom" placeholder="Prenom" size="sm"></b-form-input>
                </b-form-row>
                <b-form-row class="m-2">
                    <b-form-input v-model="nom" type="text" name="nom" placeholder="Nom" size="sm"></b-form-input>
                </b-form-row>
                <b-form-row class="m-2">
                    <b-form-input v-model="email" type="email" name="email" placeholder="Adresse electronique" size="sm"></b-form-input>
                </b-form-row>
                <b-form-row class="m-2">
                    <b-form-input v-model="motdepasse" type="password" name="motdepasse" placeholder="Mot de passe" size="sm"></b-form-input>
                </b-form-row>
                <b-form-row class="m-2">
                    <b-form-input v-model="repeter_motdepasse" type="password" name="repeter_motdepasse" placeholder="Repeter votre mot de passe" size="sm"></b-form-input>
                </b-form-row>
                <b-form-row class="m-2">
                    <b-form-checkbox v-model="accepted" name="accepter_conditions" value="accepted" size="sm">
                        <small class="m-0 p-0">
                            J'ai lu et j'accepte la politique de confidentialité et les conditions d'utilisation
                        </small>
                    </b-form-checkbox>
                </b-form-row>
                <b-form-row class="m-2" id="btnPlace">
                  <b-button type="submit" id="btnInscription" size="sm" class="pr-4 pl-4">S'inscrire</b-button>
                </b-form-row>
                <b-form-row class="m-2">
                    <small class="m-0 p-0">
                        Vous possedez un compte? Connectez-vous maintenant
                    </small>
                </b-form-row>
                </b-form>
            </b-col>
        </b-row>
    </b-modal>
  </div>
</template>
<style scoped>
  small{
        font-size: 12px;
    }
  b-form-row{
      margin: 2%;
      padding: 1%;
    }
  #btnInscription{
    background-color: #F19E33;
    border-block-color: #F19E33;
    border-block-width: 1px;
  }
  #btnPlace{
    display: flex;
    flex-direction: row;
    justify-content: center;
  }
</style>

<script>
  export default {
    name: 'Inscription',
    
  }
</script>
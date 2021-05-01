<template>
  <div>
    <b-button v-b-modal.modal-connexion>Connexion</b-button>

    <b-modal
      id="modal-connexion" centered hide-footer
      ref="modal"
    >
        <b-row style="margin: 0px;">
            <b-col cols="4" style="display:flex; flex-direction: row; justify-content:center; background: linear-gradient(#F19E33, #9d1989);">
                   <b-navbar-brand class="m-0 p-0"><img class="logo" width="100%" src="../assets/Logo.png" style="margin-top: 60%;"></b-navbar-brand>
            </b-col>
            <b-col cols="8" align-content="center">
              <b-form>
                <b-form-row class="m-1">
                  <b-col name="icone" cols="2" class="h1 mb-0">
                    <b-icon icon="person" style="color:#9d1989"></b-icon>
                  </b-col>
                  <b-col name="scripts">
                    <b-row>
                      <h6 class="m-0 ml-2 p-0">Connexion</h6>
                      <small class="m-0 ml-2 p-0">
                        Entrer votre adresse mail et votre mot de passe pour vous connecter
                      </small>
                    </b-row>
                  </b-col>
                </b-form-row>
                <b-form-row class="m-2">
                    <b-form-input v-model="email" type="email" name="email" placeholder="Adresse electronique" size="sm"></b-form-input>
                </b-form-row>
                <b-form-row class="m-2">
                    <b-form-input v-model="motdepasse" type="password" name="motdepasse" placeholder="Mot de passe" size="sm"></b-form-input>
                </b-form-row>
                <b-form-row class="m-2" >
                  <b-col cols="6" class="m-0 p-0">
                    <b-form-checkbox v-model="reminder" name="souvenir_de_moi" value="accepted" size="sm">
                      <small class="m-0 p-0">
                      Se souvenir de moi
                      </small>
                    </b-form-checkbox>
                  </b-col>
                  <b-col cols="6" class="m-0 p-0">
                    <small class="m-0 p-0">
                      Mot de passe oublié?
                    </small>
                  </b-col>
                </b-form-row >
                <b-form-row class="m-2" id="btnPlace">
                  <b-button type="submit" size="sm" id="btnConnexion" class="pl-3 pr-3">Se connecter</b-button>
                </b-form-row>
                <b-form-row class="m-2">
                  <small>
                    Vous ne disposez pas encore d'un compte? Inscrivez vous ici dès maintenant 
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

    #btnConnexion{
      background-color: #F19E33;
    }
    #btnPlace{
      display: flex;
      flex-direction: row;
      justify-content: center;
  }

</style>

<script>
  export default {
    name: 'Connexion',
  }
</script>
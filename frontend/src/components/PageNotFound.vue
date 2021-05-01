<template>
    <div class="row c404">
        <div class="col-9">
            <div class="card cc404 card-transparent mb-5">
                <div class="card-img-wrapper">
                    <div class="card-badges card-badges-bottom">
                        <span class="badge badge-pill badge-warning mt-2" style="font-size:1.4em; background-color:#9D1989; color:#fff;">404 error</span>
                    </div>
                    <img src="../assets/404.png" class="card-img-top rounded" alt="...">
                </div>
                <div class="card-body text-center">
                    <h5 class="card-title" style="color:#9D1989; font-weight:bold;font-size:1.3em;">OOPS!!!</h5>
                    <p class="card-text" style="font-size:1.2em;">La page que vous recherchez semble introuvable, revenir à l'accueil.</p>
                    <router-link to="/Home"></router-link>
                    <b-button pill class="mt-1 homeBtn" ><a id="hometext" href="/Home">Page d'accueil</a></b-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name:"PageNotFound",
}
</script>
<style scoped>
.cc404{
    margin-left: 40%;
}

.c404{
    padding-top: 1%;
}

.homeBtn{
    background-color: #F18E33;

}

#hometext{
    text-decoration: none;
    color: #fff;
    font-weight: bold;
}

</style>
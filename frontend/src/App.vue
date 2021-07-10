<template>
    <div>
        <router-view/>
    </div>
</template>

<script>
import SignUpSystem from "@/components/auth/SignUpSystem";

export default {
    name: 'App',
    created() {
        if(this.auth) this.goMainPage();
        else this.login();
    },
    computed: {
        auth: () => {
            if(localStorage.getItem('auth_token')){
                return true;
            } else {
                return false;
            }
        }
    },
    methods: {
        login() {
            this.$router.push({name: "login"})
        },
        goMainPage() {
            this.$router.push({name: "MainPage"})
        }
    }
}
</script>

<style lang="less">

#app {
    margin: 0;
    padding: 0;
    font-family: 'Roboto', sans-serif;
}

body {
    margin: 0;
}

.container{
    width: 90%;
    max-width: 1300px;
    box-sizing: border-box;
    margin: 0 auto;
}


</style>


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
        if (this.auth) this.goMainPage();
        else this.login();
    },
    computed: {
        auth: () => {
            if (localStorage.getItem('auth_token')) {
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

.container {
    width: 90%;
    max-width: 1300px;
    box-sizing: border-box;
    margin: 0 auto;
}

.standard {
    &_h1 {
        font-size: 20px;
    }

    &_header {
        width: 100%;
        box-sizing: border-box;
        background: white;
        border-radius: 15px;
        padding: 10px 10px 10px 35px;
        color: #71A6FD;
        font-weight: bold;
        font-size: 20px;
        position: relative;
        cursor: pointer;
        user-select: none;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.25);
        outline: none;
        border: none;

        &:after {
            content: "";
            background: #71A6FD;
            position: absolute;
            top: 0;
            left: 0;
            width: 25px;
            height: 100%;
            border-radius: 15px 0 0 15px;
        }
    }
}


</style>


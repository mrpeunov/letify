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
    width: 100%;
    box-sizing: border-box;
    padding: 0 200px;
}

.login_container {
    background: #ACECC3;
    width: 100%;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

h1 {
    text-align: center;
    font-weight: 400;
    margin-bottom: 30px;
}

.content {
    background: white;
    width: 100%;
    max-width: 1000px;
    height: 600px;
    border-radius: 40px;
    display: flex;
    position: relative;

    @media (max-width: 1000px) {
        width: 90%;

        .login_image {
            display: none;
        }

        .login_form {
            position: initial;
            width: 100%;
        }
    }

    .has_account {
        margin-top: 30px;
        font-size: 16px;
        font-weight: 500;
    }
}

.login {
    &_image {
        background: url("assets/img/login-bg.png") no-repeat;
        background-size: cover;
        height: 100%;
        width: calc(50% + 40px);
        border-radius: 40px 0 0 40px;
    }

    &_form {
        position: absolute;
        right: 0;
        width: 50%;
        box-sizing: border-box;
        border-radius: 40px;
        background: white;
        height: 100%;
        padding: 50px;
    }

    &_input {
        width: 100%;
        outline: none;
        border: none;
        border-bottom: solid 2px #71A6FD;
        padding-left: 20px;
        box-sizing: border-box;
        position: relative;

        &_wrap {
            margin-bottom: 20px;
        }

        &_title {
            font-size: 16px;
            font-weight: 500;
        }

        &_status {
            height: 15px;
            font-size: 12px;
            color: rgba(0, 0, 0, 0.5);
        }
    }

    &_button {
        width: 100%;
        background: linear-gradient(90deg, #10D4FF -3.53%, #00FF5B 124.4%);
        box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 20px;
        color: white;
        font-size: 18px;
        border: none;
        outline: none;
        height: 50px;
        cursor: pointer;
        margin-top: 30px;

        &:hover {
            background: linear-gradient(270deg, #10D4FF 7.9%, #00FF5B 114.32%);
        }
    }
}

.status {
    position: absolute;

    &_ok {
        &:after {
            content: '';
            display: block;
            width: 24px;
            height: 20px;
            background-size: contain;
            margin-left: -24px;
            background: url("assets/img/ok.png") no-repeat;
        }
    }

    &_error {
        &:after {
            content: '';
            display: block;
            width: 24px;
            background-size: contain;
            height: 25px;
            margin-left: -23px;
            background: url("assets/img/error.png") no-repeat;
        }
    }

    &_show {
        &:after {
            content: '';
            display: block;
            height: 20px;
            background-size: contain;
            margin-left: -23px;
            background: url("assets/img/show.png") no-repeat;
            cursor: pointer;
        }
    }

    &_hide {
        &:after {
            content: '';
            display: block;
            height: 20px;
            background-size: contain;
            margin-left: -23px;
            margin-top: -2px;
            background: url("assets/img/hide.png") no-repeat;
            cursor: pointer;
        }
    }
}
</style>


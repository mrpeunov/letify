<template>
    <div class="login_form">
        <h1>Добро пожаловать!</h1>
        <form @submit.prevent="">
            <div class="login_input_wrap">
                <div class="login_input_title">Логин или e-mail</div>
                <input
                    v-model="loginOrMail"
                    type="text" class="login_input" id="login" placeholder="username">
                <label for="login" class="status status_ok"></label>
                <div class="login_input_status"></div>
            </div>
            <div class="login_input_wrap">
                <div class="login_input_title">Password</div>
                <input
                    v-model="password"
                    type="password" id="password" class="login_input" placeholder="********">
                <label for="password" class="status status_show"></label>
                <div class="login_input_status">минимум 8 символов: цифры и буквы, на латинице и строчные</div>
            </div>
            <button class="login_button" @click="login">Войти</button>
        </form>
        <div class="has_account">Нет аккаунта?
            <router-link :to="{ name: 'signup'}">Зарегистрироваться</router-link>
        </div>
    </div>
</template>

<script>
import {loginInSystem} from "@/services/auth_api";

export default {
    name: "LoginSystem",
    data() {
        return {
            loginOrMail: "",
            password: ""
        }
    },
    methods: {
        login() {
            loginInSystem(this.loginOrMail, this.password, this.loginSuccess);
        },
        loginSuccess(){
            this.$router.push({name: "MainPage"})
        }
    }
}
</script>

<style lang="less" scoped>


</style>
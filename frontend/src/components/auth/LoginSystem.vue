<template>
    <div class="container">
        <div class="content">
            <div class="login_image">
            </div>
            <div class="login_form">
                <h1>Добро пожаловать!</h1>
                <form>
                    <div class="login_input_wrap">
                        <div class="login_input_title">Логин или e-mail</div>
                        <input
                            v-model="loginOrMail"
                            type="text" class="login_input" id="login" placeholder="username">
                        <label for="login" class="status status_error"></label>
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
                <div class="has_account">Нет аккаунта? <router-link :to="{ name: 'signup'}">Зарегистрироваться</router-link></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "LoginSystem",
    data(){
        return {
            loginOrMail: "",
            password: ""
        }
    },
    methods: {
        login() {
            console.log("Здрасте");
        }
    }
}
</script>

<style lang="less" scoped>




</style>
<template>
    <div class="container">
        <div class="content">
            <div class="login_image">
            </div>
            <div class="login_form">
                <h1>Добро пожаловать!</h1>
                <form>
                    <div class="login_input_wrap">
                        <div class="login_input_title">Логин</div>
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
                    <button class="login_button">Зарегистрироваться</button>
                </form>
                <div class="has_account">Есть аккаунт? <router-link to="login">Войти</router-link></div>
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
    created() {
        console.log("fff")
    },
    methods: {
        login() {
            console.log("здрасте")
            this.$router.push({name: "Login"})
        }
    }
}
</script>

<style lang="less" scoped>




</style>
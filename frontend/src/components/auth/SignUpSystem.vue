<template>

    <div class="login_form">
        <h1>Добро пожаловать!</h1>
        <form @click.stop>
            <div class="login_input_wrap">
                <div class="login_input_title">Логин</div>
                <input
                        v-model="login"
                        type="text" class="login_input" id="login" placeholder="username">
                <label for="login" class="status status_error"></label>
                <div class="login_input_status"></div>
            </div>
            <div class="login_input_wrap">
                <div class="login_input_title">E-mail</div>
                <input
                        v-model="mail"
                        type="text" id="email" class="login_input" placeholder="name@mail.ru">
                <label for="email" class="status status_ok"></label>
                <div class="login_input_status">аккаунт на указанный адрес уже зарегистрирован</div>
            </div>
            <div class="login_input_wrap">
                <div class="login_input_title">Password</div>
                <input
                        v-model="password"
                        type="password" id="password" class="login_input" placeholder="********">
                <label for="password" class="status status_show"></label>
                <div class="login_input_status">минимум 8 символов: цифры и буквы, на латинице и строчные</div>
            </div>
            <button class="login_button" @click.prevent="signUp">Зарегистрироваться</button>
        </form>
        <div class="has_account">Есть аккаунт?
            <router-link :to="{ name: 'login'}">Войти</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: "SignUpSystem",
    data() {
        return {
            login: "",
            mail: "",
            password: ""
        }
    },
    methods: {
        signUp() {
            console.log("регистрация");

            if(this.validateData()){
                console.log("данные валидны")
            }
        },
        validateData(){
            return true;
        }
    }
}
</script>

<style lang="less" scoped>

</style>
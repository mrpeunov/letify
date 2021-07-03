<template>
    <div class="container">
        <div class="content">
            <div class="left_image">
            </div>
            <div class="right_login">
                <form>
                    <h1>Добро пожаловать!</h1>
                    <div class="input_wrap">
                        <div class="input_title"></div>
                        <input type="text" class="input">
                        <div class="input_status"></div>
                    </div>
                    <div class="input_wrap">
                        <div class="input_title"></div>
                        <input type="text" class="input">
                        <div class="input_status"></div>
                    </div>
                    <div class="input_wrap">
                        <div class="input_title"></div>
                        <input type="password" class="input">
                        <div class="input_status"></div>
                    </div>
                    <button>Зарегистрироваться</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "LoginSystem"
}
</script>

<style lang="less" scoped>

.container {
    background: #ACECC3;
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.content {
    background: white;
    width: 100%;
    max-width: 1000px;
    height: 80vh;
    max-height: 600px;
    border-radius: 40px;
    display: flex;
    position: relative;
}

.left_image {
    background: url("../assets/img/login-bg.png") no-repeat;
    background-size: cover;
    height: 100%;
    width: calc(50% + 40px);
    border-radius: 40px 0 0 40px;
}

.right_login {
    position: absolute;
    right: 0;
    width: 50%;
    box-sizing: border-box;
    border-radius: 40px;
    background: white;
    height: 100%;
    padding: 30px;
}

.margin{

}


</style>
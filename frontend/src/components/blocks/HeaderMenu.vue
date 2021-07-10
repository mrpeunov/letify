<template>
    <div class="menu">
        <div class="menu_container">
            <div class="menu_info">
            <div class="menu_logo">
                <img src="@/assets/img/logo.png" alt="">
            </div>

            <router-link
                to="/"
                class="menu_item"
                :class="{active: isMain}">Главная</router-link>

            <router-link
                to="/competitions/"
                class="menu_item"
                :class="{active: isCompetitions}">Создание соревнований</router-link>
            <router-link
                to="/tasks/"
                class="menu_item"
                :class="{active: isTasks }">Задачи</router-link>
        </div>
            <div class="menu_lk">
            <div class="menu_lk_img">ПВ</div>
            <div class="menu_lk_name">
                Виталий Пеунов
            </div>
            <div class="menu_lk_mark">

            </div>
            <div class="menu_lk_dropdown">
                <div class="menu_lk_dropdown_item">Профиль</div>
                <div class="menu_lk_dropdown_item">Выход</div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "HeaderMenu",
    props: ['pageName'],
    computed: {
        isMain () {
            console.log("Здрасьтке")
            return this.pageName === "main";
        },
        isTasks () {
            return this.pageName === "tasks";
        },
        isCompetitions () {
            return this.pageName === "competitions";
        }
    },
    methods: {
    }
}
</script>

<style lang="less" scoped>
.menu {
    background: #F3F3F3;
    width: 100%;
    box-sizing: border-box;

    &_container{
        width: 95%;
        max-width: calc(100% - (100% - 1300px) / 2);
        margin-left: auto;
        display: flex;
        justify-content: space-between;
        height: 80px;

    }

    &_info {
        display: flex;
    }

    &_logo{
        width: 80px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 30px;

        img{
            width: 100%;
        }
    }

    &_item{
        padding: 0 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        text-decoration: none;
        color: black;

        &.active, &:hover{
            font-weight: bold;
            color: #71A6FD;
        }

        :hover{

        }
    }

    &_lk{
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 50px;

        &_img{
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-weight: 700;
            margin: 0 20px;
            background: linear-gradient(226.99deg, #59FF94 -139.65%, #56CAFC 119.66%);
        }

        &_name{
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
        }

        &_dropdown{
            display: none;
        }
    }
}
</style>
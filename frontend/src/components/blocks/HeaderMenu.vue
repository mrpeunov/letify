<template>
    <div class="menu">
        <div class="menu_container">
            <div class="menu_icon">
                <img src="@/assets/img/menu.png" alt="">
                <div class="menu_mobile">

                </div>
            </div>

            <div class="menu_info">
                <div class="menu_logo">
                    <img src="@/assets/img/logo.png" alt="">
                </div>
                <div class="menu_links">
                    <router-link
                        to="/"
                        class="menu_item"
                        :class="{active: isMain}">Главная
                    </router-link>

                    <router-link
                        to="/competitions/"
                        class="menu_item"
                        :class="{active: isCompetitions}">Создание соревнований
                    </router-link>
                    <router-link
                        to="/tasks/"
                        class="menu_item"
                        :class="{active: isTasks }">Задачи
                    </router-link>
                </div>
            </div>

            <div class="menu_lk">
                <div class="menu_lk_user">
                    <div class="menu_lk_img">ПВ</div>
                    <div class="menu_lk_name">
                        Виталий Пеунов
                    </div>
                    <div class="menu_lk_mark">

                    </div>
                </div>
                <div class="menu_lk_dropdown">
                    <router-link
                        to="/user/"
                        class="menu_lk_dropdown_item">Профиль
                    </router-link>
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
        isMain() {
            console.log("Здрасьтке")
            return this.pageName === "main";
        },
        isTasks() {
            return this.pageName === "tasks";
        },
        isCompetitions() {
            return this.pageName === "competitions";
        }
    },
    methods: {}
}
</script>

<style lang="less" scoped>
.menu {
    background: #F3F3F3;
    width: 100%;
    box-sizing: border-box;

    &_container {
        width: 95%;
        max-width: calc(100% - (100% - 1300px) / 2);
        margin-left: auto;
        display: flex;
        justify-content: space-between;
        height: 80px;

        @media (max-width: 900px){
            width: 100%;
            padding: 0 10px;
            box-sizing: border-box;
        }
    }

    &_links{
        display: flex;

        @media (max-width: 900px){
            display: none;
        }
    }

    &_icon{
        display: none;
        width: 25px;
        padding: 10px;

        img{
            width: 100%;
        }

        @media (max-width: 900px){
            display: flex;
            align-items: center;
            cursor: pointer;
        }
    }

    &_info {
        display: flex;
    }

    &_logo {
        width: 80px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 30px;

        img {
            width: 100%;
        }
    }

    &_item {
        padding: 0 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        text-decoration: none;
        color: black;

        &.active, &:hover {
            font-weight: bold;
            color: #71A6FD;
        }
    }

    &_lk {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 50px;
        cursor: pointer;

        @media (max-width: 900px){
            margin-right: 0;
        }

        &_img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-weight: 700;
            margin-right: 20px;
            background: linear-gradient(226.99deg, #59FF94 -139.65%, #56CAFC 119.66%);

            @media (max-width: 900px){
                margin-right: 0;
            }
        }

        &_name {
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;

            @media (max-width: 900px){
                display: none;
            }
        }

        &:hover .menu_lk_dropdown {
            display: block;
        }

        &:active  .menu_lk_dropdown {
            display: block;
        }

        &_user {
            display: flex;
        }

        &_dropdown {
            position: absolute;
            background: white;
            display: none;
            top: 100%;
            width: 100%;
            min-width: 150px;
            right: 0;
            text-align: center;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
            border-radius: 0 0 21px 21px;
            padding: 0 10px;
            box-sizing: border-box;

            &_item {
                padding: 15px;
                border-bottom: 2px solid #71A6FD;
                cursor: pointer;
                display: block;
                color: black;
                text-decoration: none;

                &:hover {
                    font-weight: 600;
                }

                &:last-child {
                    border-bottom: none;
                }
            }
        }
    }
}
</style>
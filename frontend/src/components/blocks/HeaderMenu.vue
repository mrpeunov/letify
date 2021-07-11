<template>
    <div class="menu">
        <div class="menu_container">

            <div class="menu_icon" @click="openMenu">
                <img src="@/assets/img/menu.png" alt="">
            </div>

            <div class="menu_wrap">
                <div class="menu_wrap_logo">
                    <img src="@/assets/img/logo.png" alt="">
                </div>

                <div class="menu_wrap_links">
                    <router-link
                        v-for="link in desktopLinks"
                        class="menu_wrap_links_item"
                        :key="link.text"
                        :to="link.href"
                        :class="{active: isLinkActive(link.name)}">{{ link.text }}
                    </router-link>
                </div>
            </div>

            <div class="menu_lk">
                <div class="menu_lk_user">
                    <div class="menu_lk_img">ПВ</div>
                    <div class="menu_lk_name">Виталий Пеунов</div>
                    <div class="menu_lk_mark"></div>
                </div>

                <div class="menu_lk_dropdown">
                    <router-link
                        v-for="link in userLinks"
                        class="menu_lk_dropdown_item"
                        :key="link.text"
                        :to="link.href">{{ link.text }}
                    </router-link>
                    <div class="menu_lk_dropdown_item" @click="goOut">Выход</div>
                </div>
            </div>
        </div>
        <div class="menu_mobile" :class="{active: openMobileMenu}">
            <router-link
                v-for="link in mobileLinks"
                class="menu_mobile_item"
                :key="link.text"
                :to="link.href"
                :class="{active: isLinkActive(link.name)}">{{ link.text }}
            </router-link>
            <div class="menu_mobile_item" @click="goOut">Выход</div>
        </div>
    </div>
</template>

<script>
export default {
    name: "HeaderMenu",
    props: ['pageName'],
    data() {
        return {
            desktopLinks: [
                {href: '/', text: "Главная", name: "main"},
                {href: '/competitions/', text: "Создание соревнований", name: "competitions"},
                {href: '/tasks/', text: "Задачи", name: "tasks"},
            ],
            userLinks: [
                {href: '/user/', text: "Профиль", name: "user"}
            ],
            openMobileMenu: false
        }
    },
    computed: {
        mobileLinks() {
            return this.desktopLinks.concat(this.userLinks);
        }
    },
    methods: {
        isLinkActive(linkName) {
            return this.pageName === linkName;
        },
        openMenu() {
            this.openMobileMenu = !this.openMobileMenu;
        },
        goOut() {
            console.log("Вылетаем из системы")
        }
    }
}
</script>

<style lang="less" scoped>
@menu-bg: #F3F3F3;

.menu {
    background: @menu-bg;
    width: 100%;
    box-sizing: border-box;

    &_container {
        width: 95%;
        max-width: calc(100% - (100% - 1300px) / 2);
        margin-left: auto;
        display: flex;
        justify-content: space-between;
        height: 80px;

        @media (max-width: 900px) {
            width: 100%;
            padding: 0 10px;
            box-sizing: border-box;
        }
    }

    &_icon {
        display: none;
        width: 30px;
        padding: 10px;

        img {
            width: 100%;
        }

        @media (max-width: 900px) {
            display: flex;
            align-items: center;
            cursor: pointer;
        }
    }

    &_wrap {
        display: flex;

        &_links {
            display: flex;

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

            @media (max-width: 900px) {
                display: none;
            }
        }

        &_logo {
            width: 80px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-right: 30px;

            @media (max-width: 900px) {
                margin: 0;
            }

            img {
                width: 100%;
            }
        }
    }

    &_lk {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 50px;
        cursor: pointer;


        @media (max-width: 900px) {
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

            @media (max-width: 900px) {
                margin-right: 0;
            }
        }

        &_name {
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;

            @media (max-width: 900px) {
                display: none;
            }
        }

        &:hover .menu_lk_dropdown {
            display: block;
        }

        &:active .menu_lk_dropdown {
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
            z-index: 10;

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

    &_mobile {
        display: none;
        position: fixed;
        height: 100vh;
        width: 100%;
        background: @menu-bg;

        &.active {
            display: block;
        }

        &_item {
            display: block;
            text-align: center;
            margin: 0 auto;
            padding: 15px;
            color: black;
            text-decoration: none;

            &:hover {
                font-weight: 600;
            }
        }
    }
}

</style>
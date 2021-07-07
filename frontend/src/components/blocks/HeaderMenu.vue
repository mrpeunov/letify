<template>
    <div class="menu">
        <div class="menu_info">
            <div class="menu_logo">
                <img src="@/assets/img/logo.png" alt="">
            </div>
            <div class="menu_item active">Главная</div>
            <div class="menu_item">Создание соревнований</div>
            <div class="menu_item">Задачи</div>
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
</template>

<script>
export default {
    name: "HeaderMenu"
}
</script>

<style lang="less" scoped>
.menu {
    background: #F3F3F3;
    width: 100%;
    height: 80px;
    padding-left: 200px;
    box-sizing: border-box;
    display: flex;
    justify-content: space-between;

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
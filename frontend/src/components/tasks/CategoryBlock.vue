<template>
    <div class="category" :class="{active: isOpen}">
        <div class="category_header" @click="toggleCategory">
            {{ title }}
        </div>
        <div class="category_items">
            <div
                v-for="task in tasks"
                :key="task.id"
                class="task">
                <div class="task_title">{{ task.title }}</div>
                <div class="task_grade">Максильная оценка: {{ task.grade }} баллов</div>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: "CategoryBlock",
    props: ['title'],
    data() {
        return {
            isOpen: true,
            isActive: true,
            tasks: [
                {id: 1, title: "Сколько фруктов?", grade: 5},
                {id: 2, title: "Сколько денег?", grade: 4},
                {id: 3, title: "Сколько лет?", grade: 4},
                {id: 4, title: "Какие планы на лето?", grade: 4},
                {id: 5, title: "Почем айфон брал?", grade: 4},
                {id: 6, title: "C++ или Python?", grade: 4},
                {id: 7, title: "ЛЭТИ или сиди?", grade: 4}
            ],
        }
    },
    methods: {
        toggleCategory() {
            console.log("Категория")
            this.isOpen = !this.isOpen;
        }
    }
}
</script>

<style lang="less" scoped>

.category {
    background: #E2E2E2;
    margin: 30px 0;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-radius: 15px;

    &_header {
        background: white;
        border-radius: 15px;
        padding: 10px 10px 10px 35px;
        color: #71A6FD;
        font-weight: bold;
        font-size: 20px;
        position: relative;
        cursor: pointer;
        user-select: none;

        &:after {
            content: "";
            background: #71A6FD;
            position: absolute;
            top: 0;
            left: 0;
            width: 25px;
            height: 100%;
            border-radius: 15px 0 0 15px;
        }
    }

    &.active {
        .category_items {
            display: grid;
        }
    }

    &_items {
        display: none;
        grid-template-columns:  1fr 1fr 1fr;
        column-gap: 50px;
        row-gap: 50px;
        padding: 50px;
    }
}

.task {
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 150px;
    border-radius: 15px;
    padding: 15px;
    background: linear-gradient(266deg, #FF2CDF -49.33%, #71A6FD 113.86%);
    box-shadow: 0 2px 9px rgba(0, 0, 0, 0.25);
    color: white;
    cursor: pointer;

    &:hover {
        background: linear-gradient(200deg, #71A6FD 113.86%, #FF2CDF -49.33%);
    }


    &_title {
        font-size: 20px;
        font-weight: 700;
    }

    &_grade {
        font-size: 14px;
        font-weight: 400;
    }
}

</style>
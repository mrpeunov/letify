<template>
    <div class="category" :class="{active: isOpen}">

        <div class="category_header" @click="toggleCategory">
            {{ title }}
        </div>
        <div class="category_items">
            <task-block v-for="task in tasks" :key="task.id" v-bind="task"></task-block>
            <div class="add_task" @click="add_task">
                <div class="add_task_blur">
                    <div class="add_task_plus">+</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import TaskBlock from "@/components/tasks/TaskBlock";

export default {
    name: "CategoryBlock",
    components: {
        TaskBlock
    },
    props: {
        title: String,
        tasks: Array
    },
    created() {
        console.log(this.title, this.tasks)
    },
    data() {
        return {
            isOpen: true,
            isActive: true,
        }
    },
    methods: {
        toggleCategory() {
            this.isOpen = !this.isOpen;
        },
        addTask(){

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
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.25);

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

.add_task{
    background: linear-gradient(266.75deg, #FFC54C -58.51%, #FF7FD5 53.28%);
    border-radius: 15px;

    &:hover{
        background: linear-gradient(266.75deg, #FF7FD5 53.28%, #FFC54C -58.51%);
    }

    &_blur{
        height: 100%;
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(4px);
        border-radius: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0px 2px 9px rgba(0, 0, 0, 0.25);
    }

    &_plus{
        font-size: 50px;
        border-radius: 50%;
        border: 3px solid black;
        display: flex;
        justify-content: center;
        align-items: center;
        @size: 50px;
        width: @size;
        height: @size;
        user-select: none;
        cursor: pointer;
        font-weight: 300;
    }
}
</style>
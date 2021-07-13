<template>
    <div class="category" :class="{active: isOpen}">

        <input class="category_header standard_header"
               v-model="componentTitle"
               @click="toggleCategory" @keyup.enter="changeName">
        <div class="category_items">
            <task-block v-for="task in tasks" :key="task.id" v-bind="task" @updatedTasks="$emit('updatedTasks')"/>
            <div class="add_task" @click="addTask">
                <div class="add_task_blur">
                    <div class="add_task_plus">+</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import TaskBlock from "@/components/tasks/main/TaskBlock";
import {changeNameCategory} from "@/services/tasks_api";

export default {
    name: "CategoryBlock",
    components: {
        TaskBlock
    },
    props: {
        id: Number,
        title: String,
        tasks: Array
    },
    data() {
        return {
            isOpen: true,
            isActive: true,
            componentTitle: this.title
        }
    },
    methods: {
        toggleCategory() {
            this.isOpen = !this.isOpen;
        },
        addTask() {
            this.$router.push({
                name: 'task-add',
                params: {category: this.id}
            })
        },
        changeName(){
            changeNameCategory(this.id, this.componentTitle, this.changedName);
        },
        changedName(){
            console.log("ff")
            this.$emit('changeNameCategory');
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

.add_task {
    background: linear-gradient(266.75deg, #FFC54C -58.51%, #FF7FD5 53.28%);
    border-radius: 15px;

    &:hover {
        background: linear-gradient(266.55deg, #FF7FD5 20.33%, #FFC54C 124.15%);
    }

    &_blur {
        height: 100%;
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(4px);
        border-radius: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0px 2px 9px rgba(0, 0, 0, 0.25);
        min-height: 150px;
    }

    &_plus {
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
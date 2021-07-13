<template>
    <div class="task" @click="openTask">
        <div class="task_title">{{ title }}</div>
        <div class="task_grade">Максильная оценка: {{ grade }} баллов</div>
        <div class="task_settings">
            <div class="task_settings_points">...</div>
            <div class="task_settings_menu">
                <div v-for="button in buttons"
                     :key="button.name"
                     @click.stop="button.func"
                     class="item"> {{ button.name}} </div>
            </div>
        </div>
    </div>
</template>

<script>
import {removeTask} from "@/services/tasks_api";

export default {
    name: "TaskBlock",
    created() {
    },
    props: {
        id: Number,
        title: String,
        grade: Number,
        withAnswer: Boolean
    },
    data(){
        return {
            buttons: [
                {name: "Изменить", func: this.change},
                {name: "Удалить", func: this.delete}
            ]
        }
    },
    methods: {
        change(){
            this.$router.push({
                name: 'task-edit',
                params: {edit: true, id: this.id}
            })
        },
        delete(){
            removeTask(this.id, this.deleted)
        },
        deleted(){
            this.$emit('updatedTasks')
        },
        openTask(){
            console.log("Открыть таск")
        },

    }
}
</script>

<style lang="less" scoped>
.task {
    display: flex;
    position: relative;
    flex-direction: column;
    justify-content: center;
    min-height: 150px;
    border-radius: 15px;
    padding: 15px;
    background: linear-gradient(266deg, #FF2CDF -49.33%, #71A6FD 113.86%);
    box-shadow: 0 2px 9px rgba(0, 0, 0, 0.25);
    color: white;
    cursor: pointer;

    &:hover{
        background: linear-gradient(266.81deg, #71A6FD -49.33%, #FF2CDF 113.86%);;
    }

    &_settings {
        position: absolute;
        right: 15px;
        top: 0;
        font-size: 30px;
        user-select: none;

        &_menu{
            display: none;
            position: absolute;
            top: 35px;
            right: 0;
            font-size: 14px;
            background: white;
            color: black;
            border-radius: 5px;

            .item{
                padding: 10px;
                width: 80px;
                text-align: center;

                &:hover{
                    font-weight: 600;
                }
            }
        }

        &:hover &_menu{
            display: block;
        }
    }

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
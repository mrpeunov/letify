<template>
    <div class="main-wrap">
        <header-menu page-name="main"></header-menu>
        <div class="container">
            <h1 class="standard_h1">Создать задачу</h1>
            <h2 class="standard_h2"><span class="elem1">1</span>Введите условие</h2>
            <div class="wrap">
                <list-variables
                    class="variables"
                    :variables="variables"
                    @addInTask="addInTask"
                    @removeVariable="removeVariable"
                    @changeVariable="changeVariable"
                />
                <add-variable
                    class="add-btn"
                    @add="addNewVariable"/>

                <div class="workspace" >
                    <textarea v-model="content"></textarea>
                </div>
            </div>

            <h2 class="standard_h2"><span class="elem2">2</span>Составьте варианты задачи</h2>
            <table-component
                :columns="variables"
                :rows="variants"
                @removeVariant="removeVariant"
                @addNewVariant="addNewVariant"/>

            <h2 class="standard_h2"><span class="elem3">3</span>Введите название и выберете оценку</h2>

            <div class="about">
                <div class="about_name">Название задачи:
                    <input type="text" class="about_input" v-model="title" placeholder="Введи название...">
                </div>
                <div class="about_name">
                    Максимальный балл:
                    <div class="about_grade">
                        <div v-for="item in grades"
                             :key="item"
                             :class="{active: grade===item}"
                             @click="grade=item"
                             class="item">{{ item }}
                        </div>
                    </div>
                </div>
            </div>
            <h2 class="standard_h2"><span class="elem4">4</span>Завершите создание</h2>
            <div
                v-if="edit"
                class="create-btn"
                @click="updateTask">Редактировать задачу</div>
            <div
                v-else
                class="create-btn"
                @click="createTask"> Создать задачу</div>
        </div>
    </div>

</template>

<script>
import HeaderMenu from "@/components/blocks/HeaderMenu";
import ListVariables from "@/components/tasks/add/ListVariables";
import AddVariable from "@/components/tasks/add/AddVariable";
import TableComponent from "@/components/tasks/add/TableComponent";
import {getTaskForEdit, sendCreatedTask, sendUpdatedTask} from "@/services/tasks_api";

export default {
    name: "AddTaskPage",
    components: {
        AddVariable,
        HeaderMenu,
        ListVariables,
        TableComponent
    },
    props:{
        category: String,
        edit: {
            type: Boolean,
            default: false
        },
        id: Number
    },
    data() {
        return {
            created: true,
            title: '',
            content: '',
            grade: '',
            variants: [{
                variables: [],
                number: 1,
                answer: ''
            }],
            grades: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }
    },
    created() {
        console.log(this.id)
        if(this.edit){
            getTaskForEdit(this.id, this.setDataForEdit)
        }
    },
    computed: {
        variables() {
            const variablesList = []

            if (this.variants.length === 0) return variablesList;

            const firstElemVariables = this.variants[0].variables;

            for (let i = 0; i < firstElemVariables.length; i++) {
                variablesList.push(firstElemVariables[i].variable)
            }

            return variablesList
        }
    },
    methods: {
        setDataForEdit(data){
            this.title = data.title;
            this.content = data.content;
            if(data.variants.length) this.variants = data.variants;
            this.grade = data.grade;
            console.log(data)
            console.log(this)
        },
        addInTask(variable) {
            this.content += "[[" + variable + "]]"
        },

        addNewVariable() {
            let newVariable = "variable" + this.variants[0].variables.length;

            //если переменная с таким именем существует добавляем в конец единичку
            while (this.variables.indexOf(newVariable) !== -1) {
                newVariable += "1"
            }

            for (let i = 0; i < this.variants.length; i++) {
                this.variants[i].variables.push({
                    "variable": newVariable,
                    "value": ''
                })
            }
        },
        changeVariable(newVariable, oldVariable) {
            while (this.variables.indexOf(newVariable) !== -1) {
                newVariable += "1"
            }

            for (let i = 0; i < this.variants.length; i++) {
                const variables = this.variants[i].variables;

                for (let j = 0; j < variables.length; j++) {
                    if (variables[j].variable === oldVariable) {
                        variables[j].variable = newVariable;
                    }
                }
            }
        },
        removeVariable(variable) {
            for (let i = 0; i < this.variants.length; i++) {
                this.variants[i].variables = this.variants[i].variables.filter(item => item.variable !== variable)
            }
        },

        addNewVariant() {
            const variant = {
                number: this.variants.length + 1,
                answer: "",
                variables: []
            }

            for (let i = 0; i < this.variables.length; i++) {
                variant.variables.push({
                    variable: this.variables[i],
                    value: ""
                })
            }

            this.variants.push(variant)
        },
        removeVariant(number) {
            if (this.variants.length === 0) return;

            if (this.variants.length === 1) {
                const variant = this.variants[0];

                variant.answer = "";

                for (let i = 0; i < variant.variables.length; i++) {
                    variant.variables[i].value = "";
                }
                console.log(variant)
                return;
            }

            //если два и более варианта, то удаляем
            this.variants = this.variants.filter(item => item.number !== number)

            //проставим варианты с первого
            for (let i = 0; i < this.variants.length; i++) {
                this.variants[i].number = i + 1;
            }
        },
        createTask(){
            sendCreatedTask(
                this.title,
                this.content,
                this.grade,
                this.category,
                this.variants,
                this.taskCreated
            )
        },
        taskCreated(data){
            if(data.status === 201) this.$router.push({name: 'tasks'})
        },
        updateTask(){
            sendUpdatedTask(
                this.title,
                this.content,
                this.grade,
                this.category,
                this.variants,
                this.id,
                this.updatedTask
            )
        },
        //далее нарушен DRY - исправить
        updatedTask(data){
            console.log(data.status)
            if(data.status === 200) this.$router.push({name: 'tasks'})
        }
    },
}
</script>

<style lang="less" scoped>

.create-btn {
    color: white;
    background: linear-gradient(270deg, #10D4FF 7.9%, #00FF5B 114.32%);
    box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
    font-weight: 500;
    cursor: pointer;
    text-align: center;
    padding: 15px;
    width: 500px;
    border-radius: 20px;
    font-size: 20px;

    &:hover{
        background: linear-gradient(90deg, #10D4FF -3.53%, #00FF5B 124.4%);
        font-weight: bold;
    }
}

.main-wrap {
    background: #FAFAFA;
    padding-bottom: 100px;
}

.about {
    &_name {
        display: flex;
        align-items: center;
        font-weight: 400;
        font-size: 18px;
        margin-bottom: 20px;
    }

    &_input {
        padding: 10px 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.25);
        margin-left: 20px;
        width: 400px;
        font-size: 18px;
        border: none;
        outline: none;
    }

    &_grade {
        display: flex;
        margin-left: 10px;

        .item {
            width: 20px;
            height: 20px;
            padding: 3px;
            border-radius: 50%;
            background: white;
            border: 1px black solid;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 5px;
            cursor: pointer;
            user-select: none;

            &.active, &:hover {
                background: #71A6FD;
                border: 1px #71A6FD solid;
                color: white;
            }
        }
    }
}

.wrap {
    display: grid;
    grid-template-areas: "variables workspace" "add-btn workspace";
    grid-template-columns: 300px 1fr;
    grid-template-rows: max(50vh, 380px) 50px;
    row-gap: 20px;
    column-gap: 50px;
    margin-bottom: 50px;
}

.variables {
    grid-area: variables;
    background: #E2E2E2;
    border-radius: 20px;
    border: 1px solid rgba(0, 0, 0, 0.15);
}

.add-btn {
    grid-area: add-btn;
}

.workspace {
    grid-area: workspace;

    textarea {
        width: 100%;
        height: 100%;
        border-radius: 10px;
        resize: none;
        outline: none;
        padding: 15px;
        box-sizing: border-box;
        font-size: 16px;
    }
}

h2 {
    display: flex;
    font-weight: 500;
    margin-top: 50px;

    span {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 25px;
        height: 25px;
        padding: 3px;

        font-size: 20px;
        border-radius: 50%;
        margin-right: 10px;
        color: white;

        &.elem1 {
            background: #FF7FD5;
        }

        &.elem2 {
            background: #FFA825;
        }

        &.elem3 {
            background: #71A6FD;
        }

        &.elem4 {
            background: #FD7070;
        }
    }
}
</style>
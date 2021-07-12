<template>
    <div>
        <header-menu page-name="main"></header-menu>
        <div class="container">
            <h1 class="standard_h1">Создать задачу</h1>

            <div class="wrap">

                <list-variables
                    class="variables"
                    :variables="variables"
                    @addInTask="addInTask"
                    @addNewVariable="addNewVariable"/>

                <add-variable
                    class="add-btn"
                    @add="addNewVariable" />

                <work-space class="workspace" ref="child"/>

            </div>

            <table-component
                :columns="variables"
                :rows="variants"
                @removeVariant="removeVariant"
                @addNewVariant="addNewVariant"/>

        </div>
    </div>

</template>

<script>
import HeaderMenu from "@/components/blocks/HeaderMenu";
import ListVariables from "@/components/tasks/add/ListVariables";
import AddVariable from "@/components/tasks/add/AddVariable";
import WorkSpace from "@/components/tasks/add/WorkSpace";
import TableComponent from "@/components/tasks/main/TableComponent";

export default {
    name: "AddTaskPage",
    components: {
        AddVariable,
        WorkSpace,
        HeaderMenu,
        ListVariables,
        TableComponent
    },
    data() {
        return {
            title: '',
            content: '',
            grade: '',
            variants: [
                {
                    "number": 1,
                    "answer": "18",
                    "variables": [
                        {
                            "variable": "a",
                            "value": "24"
                        },
                        {
                            "variable": "b",
                            "value": "6"
                        }
                    ]
                },
                {
                    "variables": [
                        {
                            "variable": "a",
                            "value": "36"
                        },
                        {
                            "variable": "b",
                            "value": "6"
                        }
                    ],
                    "number": 2,
                    "answer": "30"
                }],
        }
    },
    computed: {
        variables() {
            const variablesList = []

            if (!this.variants) return variablesList;

            const firstElemVariables = this.variants[0].variables;

            for (let i = 0; i < firstElemVariables.length; i++) {
                variablesList.push(firstElemVariables[i].variable)
            }

            return variablesList
        }
    },
    methods: {
        addInTask(variable) {
            this.$refs.child.addInText(variable)
        },
        test() {
            console.log(this.variants)
        },
        addNewVariable(variable) {
            for (let i = 0; i < this.variants.length; i++) {
                this.variants[i].variables.push({
                    "variable": variable,
                    "value": ''
                })
            }
        },
        addNewVariant() {
            const variant = {
                number: this.variants.length + 1,
                answer: "",
                variables: []
            }

            for (let item in this.variables){
                variant.variables.push({
                    variable: item,
                    value: ""
                })
            }

            this.variants.push(variant)
        },

        removeVariant(number){
            if(this.variants.length === 0) return;

            if(this.variants.length === 1){
                const variant = this.variants[0];

                variant.answer = "";

                for(let i = 0; i < variant.variables.length; i++){
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
    },
}
</script>

<style scoped>
.wrap {
    display: grid;
    grid-template-areas: "variables workspace" "add-btn workspace";
    grid-template-columns: 300px 1fr;
    grid-template-rows: 50vh 50px;
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

.add-btn{
    grid-area: add-btn;
}

.workspace {
    grid-area: workspace;
}
</style>
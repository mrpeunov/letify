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
                    @removeVariable="removeVariable"
                    @changeVariable="changeVariable"
                />

                <add-variable
                    class="add-btn"
                    @add="addNewVariable"/>

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
            created: true,
            title: '',
            content: '',
            grade: '',
            variants: [{
                variables: [],
                number: 1,
                answer: ''
            }]
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
        addInTask(variable) {
            this.$refs.child.addInText(variable)
        },
        test() {
            console.log(this.variants)
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
    },
}
</script>

<style scoped>
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
}
</style>
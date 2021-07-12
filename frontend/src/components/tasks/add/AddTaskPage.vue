<template>
    <div>
        <header-menu page-name="main"></header-menu>
        <div class="container">
            <h1 class="standard_h1">Создать задачу</h1>
            <div class="add">
                <variables-block
                    class="variables"
                    :variables="variables"
                    @addInTask="addInTask">
                </variables-block>
                <work-space class="workspace" ref="child"></work-space>
            </div>
            <table-component :columns="variables" :rows="variants"></table-component>
        </div>
    </div>

</template>

<script>
import HeaderMenu from "@/components/blocks/HeaderMenu";
import VariablesBlock from "@/components/tasks/add/VariablesBlock";
import WorkSpace from "@/components/tasks/add/WorkSpace";
import TableComponent from "@/components/tasks/main/TableComponent";

export default {
    name: "AddTaskPage",
    components: {
        WorkSpace,
        HeaderMenu,
        VariablesBlock,
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
        addNewVariable(variable){
            for (let i = 0; i < this.variants.length; i++) {
                this.variants[i].variables.push({
                    "variable": variable,
                    "value": ''
                })
            }
        }
    },
}
</script>

<style scoped>
.add {
    display: grid;
    grid-template-areas: "variables workspace";
    grid-template-columns: 300px 1fr;
    grid-template-rows: 50vh;
    row-gap: 30px;
    column-gap: 30px;
    margin-bottom: 50px;
}

.variables {
    grid-area: variables;
    background: #E2E2E2;
    border-radius: 20px;
    border: 1px solid rgba(0, 0, 0, 0.15);
}

.workspace {
    grid-area: workspace;
}
</style>
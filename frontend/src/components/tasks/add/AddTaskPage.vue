<template>
    <div>
        <header-menu page-name="main"></header-menu>
        <div class="container">
            <h1 class="standard_h1">Создать задачу</h1>
            <div class="add">
                <variables-block
                    class="variables"
                    @addInTask="addInTask">
                </variables-block>
                <work-space class="workspace" ref="child"></work-space>

                <div class="table">ff</div>
            </div>
        </div>
    </div>

</template>

<script>
import HeaderMenu from "@/components/blocks/HeaderMenu";
import VariablesBlock from "@/components/tasks/add/VariablesBlock";
import WorkSpace from "@/components/tasks/add/WorkSpace";

export default {
    name: "AddTaskPage",
    components: {
        WorkSpace,
        HeaderMenu,
        VariablesBlock
    },
    methods: {
        addInTask(variable){
            this.$refs.child.addInText(variable)
        }
    }
}
</script>

<style scoped>
.add {
    display: grid;
    grid-template-areas: "variables workspace" "table table";
    grid-template-columns: 300px 1fr;
    grid-template-rows: 50vh 1fr ;
    row-gap: 30px;
    column-gap: 30px;
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

.table {
    grid-area: table;
    background: black;
}
</style>
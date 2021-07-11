<template>
    <div class="main">
        <div class="prev">↑</div>
        <variable-item
            v-for="(variable, index) in variables"
            :key="variable"
            :name="variable"
            @remove="remove(index)"
            @addInTask="addInTask(variable)"
            class="variable"></variable-item>
        <div class="add">
            Добавить переменную
        </div>
        <div class="next">↓</div>
    </div>
</template>

<script>
import VariableItem from "@/components/tasks/add/VariableItem";

export default {
    name: "Variables",
    components: {
        VariableItem
    },
    data() {
        return {
            variables: ["count1", "count2"]
        }
    },
    methods: {
        remove(index){
            this.variables.splice(index, 1);
            console.log(this.variables)
        },
        addInTask(variable){
            console.log(variable)
            this.$emit('addInTask', variable)
        }
    }
}
</script>

<style scoped>
.main {
    background: #E2E2E2;
    border-radius: 20px;
    border: 1px solid rgba(0, 0, 0, 0.15);
}


</style>
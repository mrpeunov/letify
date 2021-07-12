<template>
    <div class="main">
        <div class="prev">
            <img src="@/assets/img/up.png" alt="">
        </div>
        <variable-item
            v-for="(variable, index) in variables"
            :key="variable"
            :name="variable"
            @remove="remove(index)"
            @addInTask="addInTask(variable)"
            class="variable"></variable-item>
        <div class="variable" @click="addVariable">
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
    props:{
        variables: Array
    },
    methods: {
        remove(index){
            //this.variables.splice(index, 1);
            //console.log(this.variables)
        },
        addInTask(variable){
            //console.log(variable)
            //this.$emit('addInTask', variable)
        },
        addVariable(){
            console.log("здесь")
            let variable = "name";
            this.$emit('addNewVariable', variable)
            //this.variables.push("")
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

.prev{
    width: 100%;
    text-align: center;
    cursor: pointer;
}

.variable {
    background: white;
    margin: 10px;
    padding: 10px;
    text-align: center;
    border-radius: 10px;
    user-select: none;
    font-weight: 700;
    cursor: pointer;
    color: #71A6FD;
    font-size: 18px;
}


</style>
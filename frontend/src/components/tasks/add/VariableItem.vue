<template>
    <div class="variable">
        <input
            v-model="variable"
            @click="addVariableInText"
            type="text"
            :readonly=edit>
        <div class="remove" @click="remove">
            <img src="@/assets/img/remove.png" alt="">
        </div>
    </div>

</template>

<script>
export default {
    name: "VariableItem",
    props: ['name'],
    created() {
        if (this.name) {
            this.variable = this.name;
        } else {
            this.variable = "Введите название"
        }
    },
    data() {
        return {
            title: '',
            edit: true
        }
    },
    methods: {
        startEdit() {
            this.edit = !this.edit
        },
        remove(){
            this.$emit('remove')
        },
        addVariableInText(){
            this.$emit('addInTask')
        }
    }
}
</script>

<style lang="less" scoped>
.variable {
    position: relative;
    background: white;
    margin: 10px;
    padding: 10px;
    text-align: center;
    border-radius: 10px;
    user-select: none;
    font-weight: 700;
    display: flex;
    cursor: pointer;

    input {
        border: none;
        text-align: center;
        outline: none;
        user-select: none;
        cursor: pointer;
        width: 90%;
        color: #71A6FD;
        font-weight: 700;
        font-size: 18px;
    }

    .remove{
        img{
            width: 15px;
        }
    }
}
</style>
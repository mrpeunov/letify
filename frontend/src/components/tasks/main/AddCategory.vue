<template>
    <div class="standard_header" @click="addCategory">
        Добавить категорию
    </div>
</template>

<script>
export default {
    name: "AddCategory",
    methods: {
        addCategory(){
            this.$emit('addCategory');
        }
    }
}
</script>

<style lang="less" scoped>
.standard_header{
    margin-bottom: 100px;
}
</style>
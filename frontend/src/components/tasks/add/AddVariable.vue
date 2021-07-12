<template>
    <div class="main" @click="$emit('add')">
        <span>+</span> Добавить переменную
    </div>
</template>

<script>
export default {
    name: "AddVariable"
}
</script>

<style lang="less" scoped>
.main {
    background: #FF7FD5;
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.25);
    color: white;
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 18px;
    font-weight: 700;
    cursor: pointer;
    transition: 0.2s;

    &:hover{
        background: white;
        color: #FF7FD5;

        span{
            font-weight: 400;
        }
    }

    span{
        color: rgba(0,0,0,0.5);
        font-weight: 300;
        font-size: 35px;
        margin-right: 10px;
    }
}
</style>
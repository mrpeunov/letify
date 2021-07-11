<template>
    <div class="workspace">
        <textarea v-model="text"></textarea>
    </div>
</template>

<script>
export default {
    name: "WorkSpace",
    data(){
        return {
            text: "Тут текст"
        }
    },
    methods: {
        addInText(variable){
            this.text += "[[" + variable + "]]"
        }
    }
}
</script>

<style lang="less" scoped>
.workspace{
    textarea{
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
</style>
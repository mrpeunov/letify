<template>
    <div class="variable">
        <input
            v-model="variable"
            @click="addVariableInText"
            ref="input"
            type="text"
            :readonly=readonly>
        <div class="variable_functions">
            <div class="variable_functions_icon" @click="startEdit">
                <img src="@/assets/img/edit.png" alt="">
            </div>
            <div class="variable_functions_icon" @click="remove">
                <img src="@/assets/img/remove.png" alt="">
            </div>
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
            readonly: true
        }
    },
    methods: {
        startEdit() {
            this.readonly = !this.readonly
            this.$refs.input.focus();
            this.$refs.input.select()
        },
        remove(){
            this.$emit('remove')
        },
        addVariableInText(){
            if(this.readonly) this.$emit('addInTask')
        }
    }
}
</script>

<style lang="less" scoped>
.variable {
    display: flex;

    input {
        border: none;
        text-align: center;
        outline: none;
        cursor: pointer;
        width: 90%;
        color: #71A6FD;
        font-weight: 700;
        font-size: 16px;
    }

    &_functions{
        &_icon{
            img{
                width: 20px;
                height: 20px;
            }
        }
    }

    .remove{
        img{
            width: 15px;
        }
    }
}
</style>
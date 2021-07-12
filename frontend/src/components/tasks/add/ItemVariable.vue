<template>
    <div class="variable">
        <input
            v-model="title"
            @click="addVariableInText"
            @keyup.enter="changeVariableName"
            ref="input"
            type="text"
            :readonly=readonly>
        <div class="variable_functions">
            <div class="variable_functions_icon" @click="startEdit">
                <img src="@/assets/img/edit.svg" alt="">
            </div>
            <div class="variable_functions_icon" @click="$emit('remove')">
                <img src="@/assets/img/basket.svg" alt="">
            </div>
        </div>

    </div>

</template>

<script>
export default {
    name: "VariableItem",
    props: {
        name: String
    },
    created() {
        this.title = this.name
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
        addVariableInText() {
            if (this.readonly) this.$emit('addInTask')
        },
        changeVariableName(){
            this.$emit('change', this.title, this.name)
        }
    }
}
</script>

<style lang="less" scoped>
.variable {
    display: flex;
    height: 50px;

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

    &_functions {
        &_icon {
            img {
                width: 20px;
                height: 20px;
            }
        }
    }

    .remove {
        img {
            width: 15px;
        }
    }
}
</style>
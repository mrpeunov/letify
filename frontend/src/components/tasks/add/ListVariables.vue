<template>
    <div class="main" ref="wrap">

        <div class="prev" @click="goUp" :class="{none: viewFirst}">
            <img src="@/assets/img/arrow-up.svg">
        </div>
        <div class="items">
            <item-variable
                v-for="variable in paginatedVariables"
                :key="variable"
                :name="variable"
                @remove="removeVariable(variable)"
                @change="changeVariable"
                @addInTask="addInTask(variable)"
                class="variable"/>
            <template v-if="!variables.length">
                <div class="empty">
                    Переменных не создано
                </div>

            </template>
        </div>
        <div class="next" @click="goDown" :class="{none: viewLast}">
            <img src="@/assets/img/arrow-down.svg">
        </div>

    </div>

</template>

<script>
import ItemVariable from "@/components/tasks/add/ItemVariable";

export default {
    name: "Variables",
    components: {
        ItemVariable
    },
    props: {
        variables: Array
    },
    data() {
        return {
            maxViewElements: 4,
            startIndex: 0
        }
    },
    created() {

    },
    mounted() {
        this.calculateMaxViewElements();
        window.addEventListener("resize", this.calculateMaxViewElements);
    },
    beforeUnmount() {
        window.removeEventListener("resize", this.calculateMaxViewElements);
    },
    computed: {
        paginatedVariables() {
            return this.variables.slice(this.startIndex, this.startIndex + this.maxViewElements)
        },
        viewFirst() {
            return this.startIndex === 0;
        },
        viewLast() {
            return this.startIndex + this.maxViewElements >= this.variables.length;
        }
    },
    methods: {
        addInTask(variable) {
            this.$emit('addInTask', variable)
        },
        goDown() {
            if (!this.viewLast) this.startIndex += 1;
        },
        goUp() {
            if (!this.viewFirst) this.startIndex -= 1;
        },
        calculateMaxViewElements() {
            if (!this.$refs.wrap) {
                return;
            }

            this.maxViewElements = (this.$refs.wrap.clientHeight - 60) / 80;
        },
        removeVariable(variable) {
            this.$emit('removeVariable', variable);
            this.goUp();
        },
        changeVariable(newVariable, oldVariable) {
            if (newVariable === oldVariable) return;
            this.$emit('changeVariable', newVariable, oldVariable)
        }
    }
}
</script>

<style scoped>
.none {
    display: none;
}

.empty{
    text-align: center;
}

.main {
    background: #E2E2E2;
    border-radius: 20px;
    border: 1px solid rgba(0, 0, 0, 0.15);
    position: relative;
}

.items {
    margin: 30px 0;
}

.prev, .next {
    width: 100%;
    text-align: center;
    cursor: pointer;
    position: absolute;
}

.prev {
    top: 0;
}

.next {
    bottom: 0;
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
<template>
    <div class="main">
        <table>
            <thead>
            <tr>
                <td>№ варианта</td>
                <td v-for="column in columns"
                    :key="column">{{ column }}
                </td>
                <td>Ответ</td>
            </tr>
            </thead>
            <tbody>
            <template v-if="rows">
                <tr v-for="row in rows" :key="row.number">
                    <td> {{ row.number }}</td>
                    <td v-for="column in row.variables" :key="column.variable">
                        <input type="text" v-model="column.value">
                    </td>
                    <td class="answer">
                        <input type="text" v-model="row.answer">
                        <img src="@/assets/img/basket.svg" alt="" @click="$emit('removeVariant', row.number)">
                    </td>
                </tr>

            </template>
            <tr>
                <td colspan="100%">
                    <div class="add_variant"
                         @click="$emit('addNewVariant')">
                        <span>+</span>Добавить вариант
                    </div>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: "TableComponent",

    props: {
        columns: Array,
        rows: Array
    },

    methods: {
        add() {
            this.$emit.addNewVariant();
        }
    },

}
</script>

<style lang="less" scoped>

.main {
    border-radius: 10px;
    box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.25);
}

.add_variant {
    color: #9F9E9E;
    line-height: 1;
    text-align: left;
    display: flex;
    align-items: center;
    cursor: pointer;

    span {
        font-size: 30px;
        font-weight: lighter;
        margin-right: 10px;
    }
}

.answer {
    position: relative;

    img {
        position: absolute;
        right: 10px;
        top: 10px;
        width: 15px;
        cursor: pointer;
    }
}

table {
    border-collapse: separate;
    border-spacing: 0;
    width: 100%;

    thead {
        background: linear-gradient(90.15deg, rgba(86, 202, 252, 0.5) -3.84%, rgba(255, 127, 213, 0.5) 112.05%);

        td {
            font-weight: 700;
            font-style: italic;
            padding: 5px;
        }

        tr:first-child {
            td:first-child {
                border-top-left-radius: 10px;
            }

            td:last-child {
                border-top-right-radius: 10px;
            }

            td {
                border-top-style: solid;
            }
        }
    }

    tbody {
        tr:last-child {
            td:first-child {
                border-bottom-left-radius: 10px;
            }

            td:last-child {
                border-bottom-right-radius: 10px;
            }
        }
    }

    td {
        border: 1px #9F9E9E;
        border-style: none solid solid none;
        text-align: center;
        padding: 5px;

        &:first-child {
            border-left-style: solid;
        }

        input {
            width: 100%;
            height: 100%;
            border: none;
            outline: none;
            font-size: 16px;
            padding: 5px;
            box-sizing: border-box;
            text-align: center;
        }
    }
}


</style>
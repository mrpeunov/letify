<template>
    <div>
        <header-menu page-name="tasks"></header-menu>
        <div class="container">
            <h1>Созданные задачи</h1>
            <div class="categories">
                <category-block
                    v-for="category in categories"
                    :title="category.title"
                    :key="category.title">
                </category-block>
            </div>
        </div>
    </div>
</template>

<script>
import HeaderMenu from "@/components/blocks/HeaderMenu";
import CategoryBlock from "@/components/tasks/CategoryBlock";

export default {
    name: "TasksPage",
    components: {
        HeaderMenu,
        CategoryBlock
    },
    data(){
        return{
            title: 'Категория стандарт',
            categories: [
                {title: 'Категория стандарт'},
                {title: 'Категория стандартес'}
            ]
        }
    }
}
</script>

<style scoped>
h1{
    font-size: 20px;
}
</style>
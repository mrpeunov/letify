<template>
    <div>
        <header-menu page-name="add_task"></header-menu>
        <div class="container" >
            <h1 class="standard_h1">Созданные задачи</h1>
            <div class="categories">
                <category-block
                    v-for="category in categories"
                    :id="category.id"
                    :title="category.title"
                    :tasks="category.tasks"
                    :key="category.title" @updatedTasks="updatedTasks()">
                </category-block>
            </div>
        </div>
    </div>
</template>

<script>
import HeaderMenu from "@/components/blocks/HeaderMenu";
import CategoryBlock from "@/components/tasks/main/CategoryBlock";
import {getCategoriesWithTasks} from "@/services/tasks_api";

export default {
    name: "TasksPage",
    components: {
        HeaderMenu,
        CategoryBlock
    },
    created() {
        this.updatedTasks()
    },
    data() {
        return {
            title: 'Категория стандарт',
            categories: []
        }
    },
    methods: {
        setCategories(categories) {
            this.categories = categories;
        },
        updatedTasks(){
            getCategoriesWithTasks(this.setCategories)
        }
    }

}
</script>

<style scoped>

</style>
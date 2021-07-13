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
            <add-category @addCategory="addCategory" />
        </div>
    </div>
</template>

<script>
import HeaderMenu from "@/components/blocks/HeaderMenu";
import CategoryBlock from "@/components/tasks/main/CategoryBlock";
import AddCategory from "@/components/tasks/main/AddCategory";
import {getCategoriesWithTasks, sendNewCategory} from "@/services/tasks_api";

export default {
    name: "TasksPage",
    components: {
        HeaderMenu,
        CategoryBlock,
        AddCategory
    },
    created() {
        this.updatedTasks()
    },
    data() {
        return {
            categories: []
        }
    },
    methods: {
        setCategories(categories) {
            this.categories = categories;
        },
        updatedTasks(){
            getCategoriesWithTasks(this.setCategories)
        },
        addCategory(){
            sendNewCategory('Новая категория', this.addedCategory)
        },
        addedCategory(data){
            this.updatedTasks()
        }
    }

}
</script>

<style lang="less" scoped>

</style>
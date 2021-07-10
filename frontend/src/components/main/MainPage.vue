<template>
    <div>
        <header-menu page-name="main"></header-menu>
        Главная
        <statistics-block></statistics-block>
    </div>
</template>

<script>
import StatisticsBlock from "@/components/main/StatisticsBlock";
import HeaderMenu from "@/components/blocks/HeaderMenu";

export default {
    name: "MainPage",
    components: {
        StatisticsBlock,
        HeaderMenu
    }
}
</script>

<style scoped>

</style>
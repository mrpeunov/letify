<template>
    <div>
        <header-menu></header-menu>
        <statistics-block></statistics-block>
    </div>
</template>

<script>
import HeaderMenu from "@/components/blocks/HeaderMenu";
import StatisticsBlock from "@/components/main/StatisticsBlock";

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
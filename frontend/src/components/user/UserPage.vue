<template>
    <div>
        <header-menu page-name="user"></header-menu>
        <div class="container">
            <blank-temporarily/>
        </div>
    </div>
</template>

<script>

import HeaderMenu from "@/components/blocks/HeaderMenu";
import BlankTemporarily from "@/components/blocks/BlankTemporarily";

export default {
    name: "UserPage",
    components: {
        HeaderMenu,
        BlankTemporarily
    }
}
</script>

<style scoped>

</style>
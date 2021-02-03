<template>
  <v-navigation-drawer fixed v-model="state.drawer" app>
    <v-list dense />
    <div class="menu">
      <div class="item"><a href="/viagens"><i class="fas fa-th" />Viagens por dia</a></div>
      <div class="item"><a href="/world"><i class="fas fa-th" />Teste</a></div>
    </div>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: ['state']
}
</script>

<style>

</style>

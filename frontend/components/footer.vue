<template>
  <v-footer color="blue-grey" class="white--text" height="28px" app>
    <span class="rodape">Powered by: Chartkick, BeautifulSoup</span>
    <v-spacer />
    <span class="rodape">2021</span>
  </v-footer>
</template>

<script>
export default {
  props: ['state']
}
</script>

<style>
v-footer {
  color: rgb(15, 124, 248);
}

.rodape {
  font-size: 13px;
}

</style>

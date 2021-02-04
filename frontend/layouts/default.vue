<template>
  <v-app id="inspire">
    <toolbar :state="layout" class="barra" /><link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600&display=swap" rel="stylesheet">
    <!-- <sidenav-left :state="layout" class="side-bar" /> -->
    <v-content class="background">
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-content>
    <le-footer />
    <v-snackbar
      :timeout="snack.timeout"
      :color="snack.color"
      bottom
      v-model="snack.visible"
    >
      {{snack.text}}
      <v-btn dark text @click.native="closeSnack">Close</v-btn>
    </v-snackbar>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js" />
    <script type="text/javascript" src="https://www.google.com/jsapi" />
  </v-app>
</template>

<script>

import Vue from 'vue'
import Chartkick from 'vue-chartkick'
import Chart from 'chart.js'
import toolbar from '~/components/toolbar.vue'
// import sidenavLeft from '~/components/sidenav-left.vue'
import footer from '~/components/footer.vue'

Vue.use(Chartkick.use(Chart))

export default {
  components: {
    toolbar,
    // sidenavLeft,
    leFooter: footer
  },
  data: () => ({
    layout: {
      drawer: false
    }
  }),
  computed: {
    snack () {
      return JSON.parse(JSON.stringify(this.$store.state.snack.snack))
    }
  },
  methods: {
    closeSnack () {
      this.$store.commit('snack/hide')
    }
  }
}
</script>

<style>
.background {
  background-image: url("../static/1614778.jpg");
  background-size: cover;
}
.contmapa {
  width: 1200px;
  padding: 20px;
  background-color: rgb(255, 255, 255);
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 40px;
  border: 8px solid #18479e;
}

.side-bar .menu .item a{
 color: #fff;
 font-size: 16px;
 text-decoration: none;
 display: block;
 padding: 5px 30px;
 line-height: 60px;
 font-family: 'Orbitron', sans-serif;
}

.side-bar .menu .item a:hover{
 /* background: #1a65aa; */
 background: rgb(15, 124, 248);
 transition: 0.3s ease;
}

.cont1 {
  background-color: lightgreen;
  display: flex;

}

</style>

<template>
  <section>
    <div>
      <v-layout justify-center align-center />

      <v-form>
        <v-container>
          <v-layout row wrap class="contmapa">
            <div style="color: black">Viagens por dia (30/01 - 03/02)</div>
            <bar-chart :data="viagens" />
            <div style="color: black">Preço das viagens do dia 30/01</div>
            <column-chart :data="precos" />
          </v-layout>
        </v-container>
      </v-form>
    </div>
  </section>
</template>

<script>

export default {
  data () {
    return {
      viagens: [['30/01', 14], ['31/01', 16], ['01/02', 16], ['02/02', 16], ['03/02', 17]],
      precos: [['07h30', 75], ['07h30-L', 95.40], ['09h30', 43], ['09h30-L', 95.40], ['09h45', 59], ['09h45-L', 130.99], ['11h45', 75], ['11h45-SL', 95.40], ['15h45', 75], ['19h30', 75], ['23h59', 49.90], ['23h59-L', 125.40]]
    }
  }
}
</script>

<style>
</style>

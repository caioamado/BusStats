<template>
  <section>
    <div>
      <v-layout justify-center align-center />

      <v-form>
        <v-container class="input_box">
          <v-layout row wrap />
          <v-flex xs12 sm6 md3>
            <v-text-field
              label="Origem"
              outline
            >
              {{dia}}
              <input type="text" v-model="novaorigem" @keyup.enter="addorigem">
            </v-text-field>
          </v-flex>
          <v-flex xs12 sm6 md3>
            <v-text-field
              label="Destino"
              outline
            />

            </v-text-field>
          </v-flex>
        </v-container>
      </v-form>
    </div>
  </section>
</template>
<script src="~/Djavue/djavue2/frontend/node_modules/js-crawler/crawler.js"></script>
<script>

import AppApi from '~api'

export default {

  data () {
    return {
      origem: 'sao-jose-dos-campos-sp',
      novaorigem: '',
      destino: 'rio-de-janeiro-todos',
      novodestino: '',
      dia: '2021-02-05'
    }
  },
  methods: {
    addorigem: function(){
      this.origem = this.novaorigem
    },
    adddestino: function(){
      this.destino = this.destino
    }
  },
  asyncData(){
    AppApi.buscrawl(origem, destino, dia).then(response =>
      console.log(response)
    )
  }
}
</script>

<style>

.input_box {
  width: 500px;
  background-color: rgb(0, 5, 73);
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 40px;
  border: 2px solid #464646;
}

.ajeitador {
display: flex;
justify-content: center;
align-items: center;
}

</style>

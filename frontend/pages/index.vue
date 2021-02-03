<template>
  <section>
    <div>
      <img src="monki.gif" v-if="loading">
      <v-layout justify-center align-center />

      <v-form>
        <v-container class="input_box">
          <v-layout row wrap />
          <v-flex xs12 sm6 md3>
            <v-text-field
              label="Origem"
              outline
              v-model="origem"
            />
          </v-flex>
          <v-flex xs12 sm6 md3>
            <v-text-field
              label="Destino"
              outline
              v-model="destino"
            />
            </v-text-field>
          </v-flex>
          <v-btn
            depressed
            elevation="2"
            rounded @click="faz_tudo()"
          >
            Analisar rota
          </v-btn>
          <v-btn
            depressed
            elevation="2"
            rounded @click="teste()"
          >
            Teste
          </v-btn>
          <section v-if="viagens[14]" style="width: 100%">
            <div>Proporção de classes de viagem</div>
            <pie-chart :data="[['Convencional', preco_classe.Convencional.length], ['Executivo', preco_classe.Executivo.length], ['SemiLeito', preco_classe.SemiLeito.length], ['Leito', preco_classe.Leito.length]]" />
            <div>Quantidade de viagens dos próximos 15 dias</div>
            <column-chart :data="dias" />
            <div>Preços da classe Convencional</div>
            <line-chart :data="preco_classe.Convencional" />
          </section>
        </v-container>
      </v-form>
    </div>
  </section>
</template>
<script>

import AppApi from '~api'

export default {

  data () {
    return {
      origem: '',
      destino: '',
      viagens: {},
      // {'daquia1':{}, 'daquia2':{}, 'daquia3':{}, 'daquia4':{}, 'daquia5':{}, 'daquia6':{}, 'daquia7':{}, 'daquia8':{}, 'daquia9':{}, 'daquia10':{}, 'daquia11':{}, 'daquia12':{}, 'daquia13':{}, 'daquia14':{}, 'daquia15':{}},
      datas: [],
      preco_classe: {'Convencional': [], 'Executivo': [], 'SemiLeito': [], 'Leito': []},
      loading: false,
      dias: []
    }
  },
  created () {
    for (let i = 1; i <= 15; i++) {
      this.datas[i - 1] = this.add_dias(i)
    }
    // for(var d=0; d<15; d++)
    // AppApi.buscrawl(this.origem, this.destino, this.datas[1]).then(response =>
    // this.viagens=response)
  },
  methods: {
    add_dias (days) {
      const result = new Date()
      result.setDate(result.getDate() + days)
      return result.toISOString().slice(0, 10)
    },
    async faz_tudo () {
      this.loading = true
      for (let d = 0; d < 15; d++) {
        // AppApi.buscrawl(this.origem, this.destino, this.datas[d]).then(response =>
        // this.viagens.push(d = response)
        // )
        const promise = AppApi.buscrawl(this.origem, this.destino, this.datas[d]).then(response =>
          response)
        const result = await promise
        this.viagens[d] = result
      }
      this.loading = false
      for (let a = 0; a < 15; a++) {
        for (let b = 0; b < Object.keys(this.viagens[a]).length; b++) {
          if (this.viagens[a][b].classe === 'Convencional') {
            this.preco_classe.Convencional.push(this.datas[a], this.viagens[a][b].preco)
          } else if (this.viagens[a][b].classe === 'Executivo') {
            this.preco_classe.Executivo.push(this.datas[a], this.viagens[a][b].preco)
          } else if (this.viagens[a][b].classe === ('Semi-Leito' || 'SEMI LEITO')) {
            this.preco_classe.SemiLeito.push(this.datas[a], this.viagens[a][b].preco)
          } else if (this.viagens[a][b].classe === 'Leito') {
            this.preco_classe.Leito.push(this.datas[a], this.viagens[a][b].preco)
          }
        }
        this.dias.push([this.datas[a], Object.keys(this.viagens[a]).length])
      }
      this.origem = ''
      this.destino = ''
    },
    teste () {
      window.console.log(this.dias)
      window.console.log(this.preco_classe)
    }
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

img {
  position: absolute;
  top: 80px;
  left: 200px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  border-radius: 10px;
  width: 90px;
  height: 90px;
  object-fit: cover;
;
}
</style>

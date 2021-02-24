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
            rounded @click="get_viagens()"
          >
            Analisar rota
          </v-btn>
          <v-btn
            depressed
            elevation="2"
            rounded @click="teste(viagens)"
          >
            Teste
          </v-btn>
          <section v-if="viagens[14]" style="width: 100%">
            <div class="titulozao">Rota  {{showorigem}}   =>   {{showdestino}}</div>
            <div class="titles">Proporção de classes de viagem</div>
            <pie-chart :data="[['Convencional', Object.keys(Convgraph.data).length], ['Executivo', Object.keys(Execgraph.data).length], ['SemiLeito', Object.keys(Slgraph.data).length], ['Leito', Object.keys(Lgraph.data).length]]" />
            <div class="titles">Quantidade de viagens dos próximos 15 dias</div>
            <column-chart :data="dias" />
            <div class="titles">Preços da classe Convencional</div>
            <line-chart :data="[Convgraph]" />
            <div class="titles">Preços da classe Executivo</div>
            <line-chart :data="[Execgraph]" />
            <div class="titles">Preços da classe Semi Leito</div>
            <line-chart :data="[Slgraph]" />
            <div class="titles">Preços da classe Leito</div>
            <line-chart :data="[Lgraph]" />
            <div class="titles">Média de preços por classe</div>
            <line-chart :data="[Avgconv, Avgexec, Avgsl, Avgl]" />
          </section>
          <v-progress-circular
            indeterminate
            color="primary" v-if="loading" style="margin-top: 10px"
          />
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
      datas: [],
      loading: false,
      dias: [],
      showorigem: '',
      showdestino: '',
      Convgraph: {name: 'Convencional', data: {}},
      Execgraph: {name: 'Executivo', data: {}},
      Slgraph: {name: 'SemiLeito', data: {}},
      Lgraph: {name: 'Leito', data: {}},
      Avgconv: {name: 'Convencional', data: {}},
      // em rotas menores alguns dias não tem viagem de uma classe específica, então na hora de fazer a média precisa começar tudo com 0
      convaux: [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
      Avgexec: {name: 'Executivo', data: {}},
      execaux: [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
      Avgsl: {name: 'SemiLeito', data: {}},
      slaux: [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
      Avgl: {name: 'Leito', data: {}},
      leitoaux: [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
      // regex função linda perfeita maravilhosa salvou minha vida
      r_conv: /Convencional/i,
      r_exec: /Executivo/i,
      r_semi: /Semi/i,
      r_leito: /Leito/i
    }
  },
  created () {
    for (let i = 1; i <= 15; i++) {
      this.datas[i - 1] = this.add_dias(i)
    }
  },
  methods: {
    add_dias (days) {
      const result = new Date()
      result.setDate(result.getDate() + days)
      return result.toISOString().slice(0, 10)
    },
    average: (array) => array.reduce((a, b) => a + b) / array.length,
    builda_graficos () {
      for (let a = 0; a < 15; a++) {
        for (let b = 0; b < Object.keys(this.viagens[a]).length; b++) {
          // arrumando a desgraça do horário que vem com 3h a menos
          const data_aux = (new Date(this.datas[a] + ' ' + this.viagens[a][b].horario)).toLocaleDateString()
          const hora_aux = (new Date(this.datas[a] + ' ' + this.viagens[a][b].horario)).toLocaleTimeString()
          if (this.viagens[a][b].classe.match(this.r_conv)) {
            // adiciona no gráfico de preço da respectiva classe
            this.Convgraph.data[data_aux + ' ' + hora_aux] = parseFloat(this.viagens[a][b].preco.slice(2).replace(',', '.'))
            // adiciona em uma matriz para fazer a média de preços desta classe nesse dia
            this.convaux[a].push(parseFloat(this.viagens[a][b].preco.slice(2).replace(',', '.')))
          } else if (this.viagens[a][b].classe.match(this.r_exec)) {
            this.Execgraph.data[data_aux + ' ' + hora_aux] = parseFloat(this.viagens[a][b].preco.slice(2).replace(',', '.'))
            this.execaux[a].push(parseFloat(this.viagens[a][b].preco.slice(2).replace(',', '.')))
            // ordem obrigatória de if-else pois o regex r_leito só checa para "leito", então se viesse antes iria incluir tanto leito quanto semi-leito
          } else if (this.viagens[a][b].classe.match(this.r_semi)) {
            this.Slgraph.data[data_aux + ' ' + hora_aux] = parseFloat(this.viagens[a][b].preco.slice(2).replace(',', '.'))
            this.slaux[a].push(parseFloat(this.viagens[a][b].preco.slice(2).replace(',', '.')))
          } else if (this.viagens[a][b].classe.match(this.r_leito)) {
            this.Lgraph.data[data_aux + ' ' + hora_aux] = parseFloat(this.viagens[a][b].preco.slice(2).replace(',', '.'))
            this.leitoaux[a].push(parseFloat(this.viagens[a][b].preco.slice(2).replace(',', '.')))
          }
        }
        // contagem de viagens por dia
        this.dias.push([this.datas[a], Object.keys(this.viagens[a]).length])
        // pega as médias de cada classe por dia e bota no objeto que o gráfico vai ler
        this.Avgconv.data[this.datas[a]] = this.average(this.convaux[a])
        this.Avgexec.data[this.datas[a]] = this.average(this.execaux[a])
        this.Avgsl.data[this.datas[a]] = this.average(this.slaux[a])
        this.Avgl.data[this.datas[a]] = this.average(this.leitoaux[a])
      }
    },
    async get_viagens () {
      this.loading = true
      this.reset_all()
      for (let d = 0; d < 15; d++) {
        const promise = AppApi.buscrawl(this.origem, this.destino, this.datas[d]).then(response =>
          response)
        const result = await promise
        this.viagens[d] = result
        window.console.log(result)
      }
      this.builda_graficos()
      this.loading = false
      this.showorigem = this.origem
      this.showdestino = this.destino
      this.origem = ''
      this.destino = ''
    },
    reset_all () {
      this.viagens = {}
      this.showorigem = ''
      this.showdestino = ''
      this.Convgraph = {name: 'Convencional', data: {}}
      this.Execgraph = {name: 'Executivo', data: {}}
      this.Slgraph = {name: 'Semi-Leito', data: {}}
      this.Lgraph = {name: 'Leito', data: {}}
      this.Avgconv = {name: 'Convencional', data: {}}
      this.convaux = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
      this.Avgexec = {name: 'Executivo', data: {}}
      this.execaux = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
      this.Avgsl = {name: 'SemiLeito', data: {}}
      this.slaux = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
      this.Avgl = {name: 'Leito', data: {}}
      this.leitoaux = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    },
    teste (str) {
      window.console.log(str)
    }
  }
}
</script>

<style>

.input_box {
  width: 500px;
  background-color: rgba(0, 1, 58, 0.897);
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
}

.titles {
  margin-top: 15px;
  margin-bottom: 8px;
  font-weight: bold;
  font-size: 20px;
}

.titulozao {
  margin-top: 15px;
  font-weight: bold;
  font-size: 35px;
}

div {
  text-align: center;
}
</style>

import Vue from 'vue'
import Router from 'vue-router'
import Index from '~/pages/index.vue'
import Todos from '~/pages/todos.vue'
import World from '~/pages/world/index.vue'
import Viagens from '~/pages/viagens/index.vue'

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  routes: [
    {path: '/', component: Index, name: 'index'},
    {path: '/todos', component: Todos, name: 'todos'},
    {path: '/world', component: World, name: 'world'},
    {path: '/viagens', component: Viagens, name: 'viagens'}
  ]
}

export function createRouter (ctx) {
  return new Router(routerOptions)
}

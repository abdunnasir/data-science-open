import Vue from 'vue'
import App from './App.vue'
import HighchartsVue from 'highcharts-vue'


Vue.use(HighchartsVue)

new Vue({
  el: '#app',
  render: h => h(App)
})
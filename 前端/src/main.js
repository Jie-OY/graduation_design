import Vue from 'vue'
import App from './App.vue'
// import ElementUI from 'element-ui'
// import 'element-ui/lib/theme-default/index.css'
import Mint from 'mint-ui'
import 'mint-ui/lib/style.css'

import store from './store'
import router from './router'




// Vue.use(ElementUI)
Vue.use(Mint)


new Vue({
  store,
  router,
  el: '#app',

  render: h => h(App)
})

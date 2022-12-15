import Vue from 'vue'
import App from './App.vue'
import VueGtag from "vue-gtag";
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import "bootstrap-icons/font/bootstrap-icons.css";

Vue.use(BootstrapVue)

Vue.use(
  VueGtag,
  {
    config: {
      id: "G-ZJBLCDESD0" ,
      params: {
        send_page_view: false,
      },
    },
  },
  router
);


Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

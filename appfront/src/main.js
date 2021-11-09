// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'default-passive-events'
import ElementUI from 'element-ui'
import Vue from 'vue'
// 引入vue-resource
import VueResource from 'vue-resource'
// 注册ElementUI组件
import '../node_modules/element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
Vue.config.productionTip = false

// 注册ElementUI组件
Vue.use(ElementUI)
    // 注册VueResource
Vue.use(VueResource)

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
        // eslint-disable-next-line eol-last
})
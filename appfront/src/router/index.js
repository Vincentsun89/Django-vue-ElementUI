import HelloWorld from '@/components/HelloWorld'
import Student from '@/components/Student'
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
export default new Router({
    routes: [{
                path: '/HelloWorld',
                name: 'HelloWorld',
                component: HelloWorld
            },
            {
                path: '/student',
                name: 'Student',
                component: Student
            }
        ]
        // eslint-disable-next-line eol-last
})
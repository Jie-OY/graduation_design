import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './components/Home.vue'
import My from './components/My.vue'
import Class from './components/Class.vue'
import Class_quiz from './components/Class_quiz.vue'
import Class_query from './components/Class_query.vue'
import Class_advice from './components/Class_advice.vue'
import Login from './components/Login.vue'

Vue.use(VueRouter)

const route = new VueRouter({
    // mode: 'history',
    routes: [
        {path: '/home', component: Home},
        {path: '/my', component: My},
        {path: '/class', component: Class,},
        // {
        //     path: '/class', component: Class,
        //     children: [
        //         {
        //             // 当 /user/quiz 匹配成功，
        //             path: 'quiz',
        //             component: Class_quiz
        //         },
        //         {
        //             // 当 /user/query 匹配成功
        //             path: 'query',
        //             component: Class_query
        //         },
        //         {
        //             // 当 /user/quiz 匹配成功，
        //             path: 'advice',
        //             component: Class_advice
        //         },
        //     ]
        // },
        {path: '/login', component: Login},
        {path: '*', redirect: '/home'}
    ],
    scrollBehavior (to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        } else {
            return {x: 0, y: 0}
        }
    }
})

export default route
import Vue from 'vue'
import Router from 'vue-router'

import Main from '@/components/Main'
import APIManagement from '@/components/APIManagement'

Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            name: 'main',
            component: Main
        },
        {
            path: '/api-management',
            name: 'api-management',
            component: APIManagement
        }
    ]
})
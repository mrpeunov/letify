import {createRouter, createWebHistory} from 'vue-router'

import MainPage from "@/components/main/MainPage";
import AuthBase from "@/components/auth/AuthBase";
import TasksPage from "@/components/tasks/TasksPage";
import CompetitionsPage from "@/components/competitions/CompetitionsPage";

const routes = [
    {
        path: '/',
        name: 'MainPage',
        component: MainPage
    },
    {
        path: '/login/',
        name: 'login',
        component: AuthBase
    },
    {
        path: '/signup/',
        name: 'signup',
        component: AuthBase
    },
    {
        path: '/tasks/',
        name: 'tasks',
        component: TasksPage
    },
    {
        path: '/competitions/',
        name: 'competitions',
        component: CompetitionsPage
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

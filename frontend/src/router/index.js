import {createRouter, createWebHistory} from 'vue-router'
import LoginSystem from "@/components/auth/LoginSystem";
import SignUpSystem from "@/components/auth/SignUpSystem";
import MainPage from "@/components/main/MainPage";
import AuthBase from "@/components/auth/AuthBase";

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
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

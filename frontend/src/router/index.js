import {createRouter, createWebHistory} from 'vue-router'
import LoginSystem from "@/components/auth/LoginSystem";
import SignUpSystem from "@/components/auth/SignUpSystem";
import MainPage from "@/components/MainPage";

const routes = [
    {
        path: '/',
        name: 'MainPage',
        component: MainPage
    },
    {
        path: '/login/',
        name: 'login',
        component: LoginSystem
    },
    {
        path: '/signup/',
        name: 'signup',
        component: SignUpSystem
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

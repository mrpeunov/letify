import {createRouter, createWebHistory} from 'vue-router'
import LoginSystem from "@/components/LoginSystem";
import SignUpSystem from "@/components/SignUpSystem";
import MainPage from "@/components/MainPage";

const routes = [
    {
        path: '/',
        name: 'MainPage',
        component: MainPage
    },
    {
        path: '/login/',
        name: 'Login',
        component: LoginSystem
    },
    {
        path: '/signup/',
        name: 'Signup',
        component: SignUpSystem
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

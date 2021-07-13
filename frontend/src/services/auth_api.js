import axios from "axios";

axios.defaults.baseURL = 'http://127.0.0.1:8000/';

export const loginInSystem = (loginOrEmail, password) => {
    getToken(password, loginOrEmail);
    /*
    * Логика такая:
    * 1. Получаем токен
    * 2. Добавляем токен в localstorage
    * 3. Добавляем в конфиг axios
    * 4. Извещаем компонент, о статусе авторизации
    * */
}

const getToken = (password, loginOrEmail) => {
    const request = {
        method: 'post',
        url: '/auth/token/login/',
        data: {
            username: loginOrEmail,
            password: password
        }
    }

    axios(request).then(function (response) {
        addTokenInLocalStorage(response.data.auth_token)
    })
}

const addTokenInLocalStorage = (token) => {
    localStorage.setItem('auth_token', token);
    axios.defaults.headers.common['Authorization'] = 'Token ' + token;
}

export const exitFromSystem = (callback) => {
    localStorage.removeItem('auth_token');
    callback()
}


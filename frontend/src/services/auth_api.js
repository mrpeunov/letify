import axios from "axios";

export const login = (password, loginOrEmail, callback) => {
    const token = getToken(password, loginOrEmail, addTokenInLocalStorage);
    //исправить
    /*
    * Логика такая:
    * 1. Получаем токен
    * 2. Добавляем токен в localstorage
    * 3. Добавляем в конфиг axios
    * 4. Извещаем компонент, о статусе авторизации
    * */
}

const getToken = (password, loginOrEmail, callback) => {
    const request = {
        method: 'GET',
        url: '',
        params: {
            password: password,
            loginOrEmail: loginOrEmail
        }
    }

    axios(request).then(function (response) {
        callback(response.data);
    });
}

const addTokenInLocalStorage = (token) => {
    localStorage.setItem('auth_token', token)
}


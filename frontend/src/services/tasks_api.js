import axios from "axios";

axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('auth_token');

export const getCategoriesWithTasks = (callback) => {
    const request = {
        method: 'get',
        url: '/api/v1/task/',
    }
    
    axios(request).then(function (response) {
        callback(response.data);
    })
}

export const sendCreatedTask = (title, content, grade, category, variants, callback) => {
    const request = {
        method: 'post',
        url: '/api/v1/task/',
        data: {
            title: title,
            content: content,
            grade: grade,
            category: category,
            variants: variants,
        }
    }

    axios(request).then(function (response) {
        callback(response.data);
    })
}
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
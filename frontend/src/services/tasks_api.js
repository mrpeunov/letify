import axios from "axios";

axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('auth_token');

export const getCategoriesWithTasks = (callback) => {
    const request = {
        method: 'get',
        url: '/api/v1/task/',
    }
    
    axios(request).then((response) => {
        callback(response.data);
    })
}

export const getTaskForEdit = (task_id, callback) => {
    const request = {
        method: 'get',
        url: `/api/v1/task/${task_id}/`,
    }

    axios(request).then((response) => {
        callback(response.data);
    })
}


export const sendUpdatedTask = (title, content, grade, category, variants, id, callback) => {
    const request = {
        method: 'patch',
        url: `/api/v1/task/${id}/`,
        data: {
            title: title,
            content: content,
            grade: grade,
            category: category,
            variants: variants,
        }
    }

    axios(request).then((response) => {
        callback(response);
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

    axios(request).then((response) => {
        callback(response.data);
    })
}

export const removeTask = (taskId, callback) => {
    const request = {
        method: 'delete',
        url: `api/v1/task/${taskId}`,
    }

    axios(request).then((response) => {
        callback(response.data)
    })
}

export const sendNewCategory = (title, callback) => {
    const request = {
        method: 'post',
        url: 'api/v1/category/',
        data: {
            title: title
        }
    }

    axios(request).then((response) => {
        callback(response.data)
    })
}

export const changeNameCategory = (categoryId, newTitle, callback) => {
    const request = {
        method: 'patch',
        url: `api/v1/category/${categoryId}/`,
        data: {
            title: newTitle
        }
    }

    axios(request).then((response) => {
        callback(response.data)
    })
}
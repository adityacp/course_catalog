import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
var BASE_URL = "http://localhost:8000"

export default axios.create({
    baseURL: BASE_URL,
    xstfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
    headers: {
        "Content-type": "application/json",
        'X-CSRFToken': 'csrftoken',
    }
});

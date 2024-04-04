import axios from 'axios';

const http = axios.create({});
http.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accesstoken');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export default http;

import axios from 'axios';

const http = axios.create({});
http.interceptors.request.use(
  (config) => {
    const accesstoken = localStorage.getItem('accesstoken');
    if (accesstoken) {
      config.headers['Authorization'] = `Bearer ${accesstoken}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export default http;
